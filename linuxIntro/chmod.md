
# chmod (Change Mode)

Used to change permissions of user, group and others.

## chmod letters:

	Operation		Permissions
	+ (add)			r (read)
	- (remove)		w (write)
	+ or -                  x (execute)

## chmod numbers:

	Number 	Permissions		       Totals
	0				---					0+0+0
	1				--x					0+0+1
	2				-w-					0+2+0
	3				-wx					0+2+1
	4				r--					4+0+0
	5				r-x					4+0+1
	6				rw-					4+2+0
	7				rwx					4+2+1

