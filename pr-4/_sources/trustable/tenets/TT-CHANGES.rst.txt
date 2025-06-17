Guidance

We expect that XYZ will need to be modified many times during its useful/production lifetime, and therefore we need to be sure that we can make changes without breaking it. In practice this means being able to deal with updates to dependencies and tools, as well as updates to XYZ itself.

Note that this implies that we need to be able to:

verify that updated XYZ still satisfies its expectations (see below), and

understand the behaviour of upstream/suppliers in delivering updates (e.g. frequency of planned updates, responsiveness for unplanned updates such as security fixes).

We need to consider the maturity of XYZ, since new software is likely to contain more undiscovered faults/bugs and thus require more changes. To support this we need to be able to understand, quantify and analyse changes made to XYZ (and its dependencies) on an ongoing basis, and to assess the XYZ approach to bugs and breaking changes.

We also need to be able to make modifications to any/all third-party components of XYZ and dependencies of XYZ, unless we are completely confident that suppliers/upstream will satisfy our needs throughout XYZ’s production lifecycle.
