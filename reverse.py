def reverse(text):
  reversed = []
  for i in range(len(text)):
    reversed.append(text[-(i+1)])

  return ''.join(reversed)
