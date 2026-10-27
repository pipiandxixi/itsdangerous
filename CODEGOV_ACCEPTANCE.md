# CodeGov GitHub acceptance scenarios

This fork contains isolated, deliberately planted CodeGov acceptance scenarios.
These are not proposed upstream fixes and must not be merged or released as product changes.
Original upstream source remains unchanged. The real project's source and Git history provide
repository context; the added codegov_acceptance directory supplies reproducible ground truth.

The trusted default-branch policy blocks new domain-to-infrastructure imports. Cycle,
code-contract and duplicate-code findings are advisory. Each PR branches independently
from this baseline, so scenarios do not contaminate one another.

| Scenario | Expected CodeGov behavior |
| --- | --- |
| Cycle and layer violation | Dependency-cycle finding, forbidden-edge finding, blocking verdict and failure conclusion |
| Required API parameter, untouched consumer | Contract-consumer finding and neutral conclusion |
| Copy existing source into a new file | Duplicate-code finding with both snippet ranges and neutral conclusion |
| Documentation-only edit | No new actionable governance findings; non-applicable or partial coverage is legitimate |
| Language boundary regression | Follow the PR's independently stated expected semantics; do not derive expectations from current analyzer output |

These fixtures do not establish all-language support, calibrated precision, actual branch protection,
or correctness of upstream project behavior. Native analysis and coverage gaps remain explicit.

This sentence is the documentation-only negative control.
