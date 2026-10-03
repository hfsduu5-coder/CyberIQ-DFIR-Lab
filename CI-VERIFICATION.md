# CI Verification

This repository contains a GitHub Actions test workflow for push, pull request, and manual `workflow_dispatch` execution.

## Evidence policy

CI is considered verified only when GitHub reports a completed successful workflow/check for the relevant commit. The existence of a workflow file is not treated as proof that CI passed.

## Current verification state

At the latest portfolio audit on 2026-10-03, the available GitHub connector returned no commit statuses and no associated pull-request workflow runs for the audited commit. Therefore no green-CI claim is made here.

## Manual verification

Open the repository's **Actions** tab, select the test workflow, choose **Run workflow** on `main`, and confirm all jobs complete successfully. Preserve the successful run as the evidence for the portfolio roadmap.
