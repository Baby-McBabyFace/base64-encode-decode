import base64
import tkinter

msg = """Welcome to Base64 Encoder/Decoder!\n\n""" + "="*20 + "\n\n"
def decode_b64():
	b64 = entryBase64.get()
	output = "Original: " + b64 + "\n\n"
	textArea.insert(tkinter.END, output)
	try:
		b64 = base64.b64decode(b64).decode('utf-8')
		output = "Decoded: " + str(b64) + "\n\n" + "="*20 + "\n\n"
		textArea.insert(tkinter.END, output)
		entryBase64.delete(0,tkinter.END)
		entryBase64.focus()
		textArea.see(tkinter.END)
	except ValueError:
		output = "Error: " + str(b64) + " is not decoded. It is invalid."+"\n\n" + "="*20 + "\n\n"
		textArea.insert(tkinter.END, output)
		entryBase64.delete(0,tkinter.END)
		entryBase64.focus()
		textArea.see(tkinter.END)

def encode_b64():
	b64 = entryBase64.get()
	output = "Original: " + b64 + "\n\n"
	textArea.insert(tkinter.END, output)
	b64 = base64.b64encode(b64.encode('utf-8'))
	output = "Encoded: " + str(b64) + "\n\n" + "="*20 + "\n\n"
	textArea.insert(tkinter.END, output)
	entryBase64.delete(0,tkinter.END)
	entryBase64.focus()
	textArea.see(tkinter.END)

root = tkinter.Tk()
root.title('Base64 Encoder/Decoder')

frame = tkinter.Frame(root)
frame.pack(side = tkinter.TOP)

bottomframe = tkinter.Frame(root)
bottomframe.pack( side = tkinter.BOTTOM )


labelBase64 = tkinter.Label(frame, font="bold", text="Paste text here: ")
labelBase64.pack(side=tkinter.LEFT)

entryBase64 = tkinter.Entry(frame)
entryBase64.pack(side=tkinter.LEFT)
entryBase64.focus()

textArea = tkinter.Text(bottomframe, background='white', font="Consolas", height=20, width=125)
textArea.pack(side=tkinter.LEFT, fill=tkinter.BOTH, anchor=tkinter.NW)
textArea.insert(tkinter.END, msg)

buttonEncode = tkinter.Button(frame, text="Encode", command=encode_b64)
buttonEncode.pack(side=tkinter.TOP)

buttonDecode = tkinter.Button(frame, text="Decode", command=decode_b64)
buttonDecode.pack(side=tkinter.TOP)

root.mainloop()
