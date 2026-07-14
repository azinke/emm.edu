# Courses are routes through the book

Courses do not own theory. They select chapters, labs, and projects from the
canonical curriculum and add only audience, pacing, prerequisites, and assessment
decisions.

- [`catalog.toml`](catalog.toml) defines prerequisites and course routes.
- [`program.toml`](program.toml) assembles the eight-semester reference program.
- [`../book/chapters.toml`](../book/chapters.toml) defines the stable body of knowledge.

An instructor preparing a course should first choose chapter IDs, then choose the
physical evidence and project integration. Lecture plans are derived last. If a
needed explanation is missing, improve the book rather than putting the
explanation in a private course directory.

The reference program is a design baseline, not an accreditation assertion.
Local institutions must approve credits, entry, assessment, safety, staffing, and
regulatory mappings.

Elective mappings marked `route_status = "example"` are coherent starting routes,
not a forced specialization. A real elective must publish its own bounded chapter,
lab, and assessment selection before delivery.
