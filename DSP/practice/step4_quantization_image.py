# DSP STEP 4 / 9  -  Quantization levels on an image   (syllabus 2c: "image file will be provided")
#
# An 8-bit grayscale image has 256 levels (0..255). Quantizing to L levels means every pixel
# snaps to one of L values. Same idea as PCM zones, applied to brightness instead of voltage:
#   step  = 256 / L                             width of one zone
#   zone  = np.floor(img / step)                0 .. L-1
#   q_img = zone * step                         bottom value of the zone   (or (zone + 0.5) * step for the middle)
# L = 2**bits.  Fewer levels -> visible banding ("posterisation"). That is what she wants you to observe.
#
# Loading: img = plt.imread("file.jpg")  -> uint8 array (H, W, 3) for colour. Convert to float first.
# Grayscale: img.mean(axis=2)   (average of R, G, B)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

<<<<<<< HEAD

path = "C:/Users/adib/Pictures/Saved Pictures/Kalapahar_29_Nov.jpg"   # in the exam: path = "whatever_she_gives.jpg"
img  = plt.imread(path).astype(float)      # (600, 512, 3), values 0..255

# TODO: grayscale image (H, W): average over the colour axis
=======
# path = cbook.get_sample_data("grace_hopper.jpg", asfileobj=False)   # in the exam: path = "whatever_she_gives.jpg"
path = "C:/Users/ADIB/Downloads/PXL_20240622_154106458.MP.jpg"
img  = plt.imread(path).astype(float)      # (600, 512, 3), values 0..255

# # TODO: grayscale image (H, W): average over the colour axis
>>>>>>> ef1da11e463049280418d6d91a236737edf5d842
gray = img.mean(axis=2)


def quantize(image, L):
    """Snap every pixel of `image` (values 0..255) to one of L levels. Returns float array, same shape."""
    step = 256 / L
    zone = np.floor(image / step)
    q_img = zone * step
    # TODO: step, zone, return zone * step
<<<<<<< HEAD
=======
    step = 256 / L
    zone = np.floor(image / step)
    q_img = zone * step
>>>>>>> ef1da11e463049280418d6d91a236737edf5d842
    return q_img


# ---------------- checker: don't edit below ----------------
ok = gray is not None and gray.shape == img.shape[:2]
levels = [2, 4, 8, 16, 256]
if ok:
    for L in levels:
        q = quantize(gray, L)
        n_unique = None if q is None else len(np.unique(q))
        good = q is not None and q.shape == gray.shape and n_unique <= L and (L > 16 or n_unique == L)
        ok &= good
        print(f"L = {L:>3} levels ({int(np.log2(L))} bits)  ->  unique pixel values: {n_unique}   {'ok' if good else 'FAIL'}")
print("PASS  ->  open step5_dt_sequences.py" if ok else "FAIL  (gray must be (H, W); quantize must return <= L distinct values)")

if ok:
    fig, axes = plt.subplots(1, len(levels) + 1, figsize=(10, 4))
    axes[0].imshow(gray, cmap="gray", vmin = 0, vmax = 255)
    axes[0].set_title("Original (256 levels)")
    for ax, L in zip(axes[1:], levels):
        ax.imshow(quantize(gray, L), cmap="gray", vmin=0,vmax=255)
        ax.set_title(f"L = {L} ({(int)(np.log2(L))} bits)")
    for ax in axes: ax.axis("off")
<<<<<<< HEAD
    plt.tight_layout()
    plt.show()












    # fig, axes = plt.subplots(1, len(levels) + 1, figsize=(16, 4))
    # axes[0].imshow(gray, cmap="gray", vmin=0, vmax=255)
    # axes[0].set_title("original (256)")
    # for ax, L in zip(axes[1:], levels):
    #     ax.imshow(quantize(gray, L), cmap="gray", vmin=0, vmax=255)
    #     ax.set_title(f"L = {L} ({int(np.log2(L))} bits)")
    # for ax in axes: ax.axis("off")
    # plt.tight_layout()
    # plt.show()
=======
    plt.tight_layout(); plt.show()
>>>>>>> ef1da11e463049280418d6d91a236737edf5d842
