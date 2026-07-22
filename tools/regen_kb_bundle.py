#!/usr/bin/env python3
"""Regenerate the NotebookLM KB bundle from docs/knowledge-base/*.md.

The bundle (docs/notebooklm/00-flipp-troubleshooting-knowledge-base.md) is a
mechanical concatenation of the general knowledge-base articles in a curated
*reading order* (NOT alphabetical), separated by a horizontal rule.

Usage:
    python3 tools/regen_kb_bundle.py            # write the bundle
    python3 tools/regen_kb_bundle.py --check    # verify current bundle matches (exit 1 if drift)

Robustness: any *.md in docs/knowledge-base/ that is not listed in ORDER is
appended at the end and a warning is printed to stderr, so a newly-added
article is never silently dropped from the bundle.
"""
import sys, os

KB_DIR = "docs/knowledge-base"
BUNDLE = "docs/notebooklm/00-flipp-troubleshooting-knowledge-base.md"

# Curated reading order. New articles: insert in the logical spot here.
ORDER = [
    "flyer-processing-overview.md",
    "content-v2-and-publishing.md",
    "codesheet-errors.md",
    "item-import-format.md",
    "turbo-cp-legacy-error-guide.md",
    "missing-flyers-and-indexing.md",
    "clipping-and-autobox.md",
    "stores-and-harmonization.md",
    "flyer-dates.md",
    "hosted-and-previews.md",
    "publishing-and-go-live.md",
    "common-live-flyer-issues.md",
    "storefront-publishing-errors.md",
    "home-depot-us-troubleshooting.md",
    "retailer-onboarding-process.md",
    "indexing-ci-baseline-tasks.md",
    "account-flyer-review-directory.md",
    "coupon-ops-verification-matching-qc.md",
    "coupon-accuracy-checks.md",
    "live-date-checks.md",
    "alert-runbooks.md",
    "home-depot-canada-dvm-module-runbook.md",
    "publisher-qa-dsp.md",
    "escalation-and-tickets.md",
    "post-escalation-what-happens-next.md",
    "glossary.md",
]

HEADER = (
    "# Flipp Flyer-Processing Troubleshooting — CXE Help Center\n\n"
    "> Combined bundle of the CXE Help Center's general troubleshooting, process, QC, and runbook guidance. "
    "For retailer-specific processing, see the \"Retailers - <letter>\" bundles and the \"CP Processing SOPs\" bundle.\n\n"
    "---"
)


def build():
    present = [f for f in os.listdir(KB_DIR) if f.endswith(".md")]
    order = list(ORDER)
    unlisted = sorted(set(present) - set(order))
    if unlisted:
        sys.stderr.write("WARNING: appending unlisted KB articles at end: %s\n" % ", ".join(unlisted))
        order += unlisted
    missing = [f for f in order if not os.path.exists(os.path.join(KB_DIR, f))]
    if missing:
        sys.stderr.write("WARNING: ORDER lists files not on disk (skipped): %s\n" % ", ".join(missing))
        order = [f for f in order if f not in missing]
    parts = []
    for fn in order:
        with open(os.path.join(KB_DIR, fn), encoding="utf-8") as fh:
            parts.append(fh.read().rstrip("\n"))
    return HEADER + "\n\n" + "\n\n\n---\n\n".join(parts) + "\n\n"


def main():
    out = build()
    if "--check" in sys.argv:
        cur = open(BUNDLE, encoding="utf-8").read() if os.path.exists(BUNDLE) else ""
        if cur == out:
            print("OK: bundle matches source articles")
            return 0
        sys.stderr.write("DRIFT: bundle does not match source articles — run without --check to regenerate\n")
        return 1
    with open(BUNDLE, "w", encoding="utf-8") as fh:
        fh.write(out)
    print("Wrote %s (%d articles)" % (BUNDLE, out.count("\n# ") + 1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
