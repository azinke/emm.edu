# Seeded KiCad failure

`seeded-short.kicad_pcb` is a syntactically valid KiCad 9 board with two coincident
pads on different nets. The release hook must invoke the real frozen `kicad-cli`,
capture the `shorting_items`/solder-mask DRC violations, and reject the project.
The five-kind smoke fixture separately proves the command interface without KiCad;
it never turns a missing real release dependency into a pass. Replace this fixture
only with another reviewed, reproducible failing project; never waive it.
