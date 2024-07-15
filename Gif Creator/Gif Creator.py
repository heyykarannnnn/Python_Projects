import imageio
filenames = ["/Users/karanmac/Desktop/VSCODE Files/Python Projects/Ready/Gif Creator/Images/1.png", "/Users/karanmac/Desktop/VSCODE Files/Python Projects/Ready/Gif Creator/Images/2.png" , "/Users/karanmac/Desktop/VSCODE Files/Python Projects/Ready/Gif Creator/Images/3.png", "/Users/karanmac/Desktop/VSCODE Files/Python Projects/Ready/Gif Creator/Images/4.png", "/Users/karanmac/Desktop/VSCODE Files/Python Projects/Ready/Gif Creator/Images/5.png", "/Users/karanmac/Desktop/VSCODE Files/Python Projects/Ready/Gif Creator/Images/6.png"]
images = []
for filename in filenames:
	images.append(imageio.imread(filename))
imageio.mimsave('/Users/karanmac/Desktop/VSCODE Files/Python Projects/Ready/Gif Creator/gif.gif', images, 'GIF', duration=1)