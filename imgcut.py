def cutimg(f,cutbyw,n,piecew,pieceh):
  r = pieceh/piecew
  cv2_image = cv2.imread(list(f.keys())[0], cv2.IMREAD_COLOR)
  y,x,c = cv2_image.shape

  if cutbyw:
    w = x//n
    h = round(w*r)
  else:
    h = y//n
    w = round(h/r)
    
  os.mkdir(f'/{list(f.keys())[0][:-4]}')
  for i in range(x//w):
    for j in range(y//h):
      cropped = cv2_image[j*h:(j+1)*h+1,i*w:(i+1)*w+1]
      cv2.imwrite(f'/{list(f.keys())[0][:-4]}/{list(f.keys())[0][:-4]}{j,i}.png',cropped)
  
