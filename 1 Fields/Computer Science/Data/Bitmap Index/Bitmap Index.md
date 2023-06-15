- A **database index** that uses bitmaps or bit arrays
- Stores a bitmap for each distinct value of an indexed column
- Each bit in the bitmap corresponds to a row in the table
- The bit is **1** if the row contains the value, and **0** otherwise
- Bitmap indexes are efficient for columns with **low cardinality**, i.e., few distinct values
- Bitmap indexes can perform fast **set-based operations** such as AND, OR, and NOT on multiple bitmaps
- Bitmap indexes are suitable for **read-only** or **infrequently updated** tables, as they have high maintenance overhead
___
Type: #subtopic 
Topics: [[Computer Science]], [[Data]]

