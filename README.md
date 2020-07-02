# PaperTapeRead
**Version 0.1**
---


## Background
I created this project to read some old paper tapes I found at home from the 1970's to 1980's. There are five sample tapes, all containing a variation of the same message, and one "error tape". The tapes have a series of lines that have 1-9 holes in them that span the shorter dimension of the tape. These holes can be transalted into binary, with a hole representing a "1". You can read more about the system here: https://iclces.uk/articles/reading_punched_paper_tape.html

## Function
This short python program reads in a text file (.txt) that has each line of holes already digitally converted to 1 and 0. In this case there are only 8 digits as one of the aforementioned holes was only used to mechanically move the tape. 

The first digit in the line (left side) will represent the parity bit. The total sum of holes in any line must be even, with the parity bit being used for any line that would otherwise be odd. This parity bit is removed, and then the other seven digits are read to get the ASCII equivalent letter/character. If the line contains an odd number of lines, an error is inserted into the string. The original machines would use this parity bit to ensure that data had been stored and read properly, so I thought I would emulate that feature. "tape5.txt" contains a manufactured error to display this feature.

## Future Work

Overall this was a very short project, but I think someone might find it useful in the future. If you could use a micro-computer to read the physical tapes and convert them into a .txt file, it would be easy to read longer messages quite quickly.

---
## Resources
How to manually read Paper Tapes: https://iclces.uk/articles/reading_punched_paper_tape.html
StackOverflow Help: https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa
