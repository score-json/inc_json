TA-UPDATES
==========

XYZ components, configurations and tools are updated under specified change and configuration management controls.

Supported Requests
------------------

TT-CHANGES

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

This assertion requires that we have control over all changes to XYZ, including changes to the configurations, components, and tools we use to build it, and the versions of dependencies that we use.

This means the trustable controlled process is the only path to production for constructed target software.

Evidence
--------

- Change management process and configuration artifacts

Confidence Scoring
------------------

Confidence scoring for TA-UPDATES is based on confidence that we have control over the changes that we make to XYZ, including its configuration and dependencies.

Checklist
---------

- Where are the change and configuration management controls specified?
- Are these controls enforced for all components, tools, and configurations?
- Are there any ways in which these controls can be subverted, and have we mitigated them?
