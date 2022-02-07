##Reverse Latin Numbers Order || Change It To Arabic
By Using This Library You Can Change Latin Numbers Order From Left to Right or change them to Arabic and store them in new file.

###Installation
```pip install latin_to_arabic_number```

### How to use it?
There are two methods:
1. latin_to_arabic(file_to_read,file_to_save) 
2. reverse_numbers_order(file_to_read,file_to_save) 

   - These methods receive two parameters:
     - file_to_read: This is the target file which changes need to apply for.
     - file_to_save: Directory To save result.


### Usage

```python
from latin_to_arabic_number import reverse_numbers_order, latin_to_arabic

file_to_read= "/tmp/personal/target_file_name.docx"
file_to_save= "/tmp/personal/new_file_name.docx"

#returns 'A new file with reversed numbers'
#If we have 'I am 28 years old' the result would be 'I am 82 years old'
reverse_numbers_order(file_to_read=file_to_read,file_to_save=file_to_save)

#returns 'A new file with changed latin numbers to arabic'
#If you have a text like 'I am 28 years old' the result would be 'I am ۲۸ years old'
latin_to_arabic(file_to_read=file_to_read,file_to_save=file_to_save) 
```


