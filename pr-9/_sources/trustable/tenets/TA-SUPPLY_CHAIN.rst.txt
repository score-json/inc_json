TA-SUPPLY_CHAIN
===============

All sources for XYZ and tools are mirrored in our controlled environment.

Supported Requests
------------------

TT-PROVENANCE

Supporting Items
----------------

None

References
----------

None

Fallacies
---------

None

Guidance
--------

This assertion is satisfied to the extent that we have traced and captured source code for XYZ and all of its dependencies (including transitive dependencies, all the way down), and for all of the tools used to construct XYZ from source. We have mirrored versions of these inputs under our control.

'Mirrored' in this context means that we maintain a version of the upstream project that is kept up-to-date with additions and changes to the upstream project but protected from changes that would delete the project or remove parts of its history.

Clearly, this is not possible for components or tools provided only in binary form or accessed via online services. In these circumstances, we can only assess confidence based on attestations made by the suppliers and our experience with the suppliers' people and processes.

Keep in mind that even if repositories with source code for a particular component or tool are available, not all of it may be stored in Git as plaintext. A deeper analysis is required in TA-INPUTS to assess the impact of any binaries present within the repositories of the components and tools used.

Evidence
--------

- List of all XYZ components, including:
  - URL of mirrored projects in controlled environment
  - URL of upstream projects
- Successful build of XYZ from source without access to external source projects and cached data
- Update logs for mirrored projects
- Mirrors reject history rewrites
- Mirroring is configured via infrastructure under direct control

Confidence Scoring
------------------

Confidence scoring for TA-SUPPLY_CHAIN is based on our confidence that all inputs and dependencies are identified and mirrored, and that mirrored projects cannot be compromised.

Checklist
---------

- Could there be other components missed from the list?
- Does the list include all toolchain components?
- Does the toolchain include a bootstrap?
- Could the content of a mirrored project be compromised by an upstream change?
- Are mirrored projects up to date with the upstream project?
