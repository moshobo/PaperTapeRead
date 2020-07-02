Project Start = July 2nd, 2020

I created this project to read some old paper tapes I found at home from the 1970's to 1980's. The tapes have a series of lines that have 1-9 holes in them that span the shorter dimension of the tape. These holes can be transalted into binary, with a hole representing a "1". You can read more about the system here: https://iclces.uk/articles/reading_punched_paper_tape.html

This short python program reads in a text file (.txt) that has each line of holes already digitally converted to 1 and 0. In this case there are only 8 digits as one of the aforementioned holes was only used to mechanically move the tape. The first digit in the line (left side) will represent the parity bit. The total sum of holes in any line must be even, with the parity bit being used for any line that would otherwise be odd. This parity bit is removed, and then the other seven digits are read to get the ASCII equivalent letter/character. 



# StackOverflow Help: https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa
