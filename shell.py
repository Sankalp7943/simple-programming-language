import simple
# loop over in shell
while True:
    text= input('simple > ')
    result, error = simple.run('<stdin>', text)
    if error: print(error.as_string())
    else: print(result)

