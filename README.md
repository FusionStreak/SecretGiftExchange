# Secret Gift Exchange

A Python script that will take in a list of names, randomly assign Secret Santas, and send each member an email containing the required info. **This is meant as a fun little personal project not a fully functional tool.**

## How To

- Create a txt file w/ the following data in this format:

```txt
name1, email1
name2, email2
...

```

- Be sure to add an extra newline at end of file
- [Turn Allow less secure apps to ON](https://myaccount.google.com/lesssecureapps)
- Run `$ py main.py`
- Input your source e-mail address
- Input your password
- Input path to the file you created above
- An email will be sent to each recipient with their match
- An encrypted string will be sent to the source e-mail along with a key

```txt
        Key: <some key>

        Matches: <some encrypted string>
```

- Use this information along with `matchesDecrypter.py` or any Fernet decrypter to get the original matches list if needed
- This information will also be printed to the console as back up
- **No information is stored or sent anywhere outside the list of emails you have provided**

## Resources

- [Sending Emails With Python](https://realpython.com/python-send-email/) from RealPython
