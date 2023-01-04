| Function                                | Description                                                                                     |
|-----------------------------------------|-------------------------------------------------------------------------------------------------|
| `cv2.imread(filename[, flags])`         | Loads an image from a file.                                                                     |
| `cv2.imwrite(filename, img[, params])`  | Saves an image to a file.                                                                       |
| `cv2.resize(src, dsize[, dst[, fx[, fy[, interpolation]]]])` | Resizes an image.                                                                            |
| `cv2.cvtColor(src, code[, dst[, dstCn]])` | Converts an image from one color space to another.                                              |
| `cv2.blur(src, ksize[, dst[, anchor[, borderType]]])`      | Blurs an image using the mean of the pixels in a square kernel.                              |
| `cv2.GaussianBlur(src, ksize, sigmaX[, dst[, sigmaY[, borderType]]])` | Blurs an image using the weighted sum of the pixels in a Gaussian kernel.                 |
| `cv2.medianBlur(src, ksize[, dst])`    | Blurs an image using the median of the pixels in a square kernel.                              |
| `cv2.line(img, pt1, pt2, color[, thickness[, lineType[, shift]]])` | Draws a line on an image.                                                                   |
| `cv2.rectangle(img, pt1, pt2, color[, thickness[, lineType[, shift]]])` | Draws a rectangle on an image.                                                              |
| `cv2.circle(img, center, radius, color[, thickness[, lineType[, shift]]])` | Draws a circle on an image.                                                                 |
| `cv2.putText(img, text, org, fontFace, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])` | Puts text on an image.                                                                      |
