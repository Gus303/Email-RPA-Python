import win32com.client as win32

outlook = win32.Dispatch('outlook.application')

email = outlook.CreateItem(0)

email.To = "gustavorochatest@outlook.com"
email.Suject = "Automatic E-mail from Python"
email.HTMLBody = """"
<h1>Hello world!</h1>

<p>Lorem Ipsum</p>

<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
</p>

<p>Bye,</p>
<p>Python</p>
"""

email.Send()
print("Email sent")