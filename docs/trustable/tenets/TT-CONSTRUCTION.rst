Guidance

Where possible we prefer to build, configure and install XYZ from source code, because this reduces (but does not eliminate) the possibility of supply chain tampering.

When constructing XYZ we aspire to a set of best practices including:

reproducible builds
construction from a given set of input source files and build instructions leads to a specific fileset

re-running the build leads to exactly the same fileset, bit-for-bit

ensuring that all XYZ dependencies are known and controlled (no reliance on external/internet resources, or unique/golden/blessed build server); and

automated build, configuration and deployment of XYZ based on declarative instructions, kept in version control (e.g. no engineer laptop in the loop for production releases)

Some of these constraints may be relaxed during XYZ development/engineering phases, but they must all be fully applied for production releases. Note that when we receive only binaries, without source code, we must rely much more heavily on Provenance; who supplied the binaries, and how can we trust their agenda, processes, timescales and deliveries?
