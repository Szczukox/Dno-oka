def statistics(binary_input_image, binary_output_image):
    tp, tn, fp, fn = 0, 0, 0, 0
    for i in range(len(binary_input_image)):
        for j in range(len(binary_input_image[0])):
            if binary_input_image[i][j][0] == 255 and binary_output_image[i][j] == 255:
                tp += 1
            elif binary_input_image[i][j][0] == 0 and binary_output_image[i][j] == 0:
                tn += 1
            elif binary_input_image[i][j][0] == 0 and binary_output_image[i][j] == 255:
                fp += 1
            elif binary_input_image[i][j][0] == 255 and binary_output_image[i][j] == 0:
                fn += 1
    tpr = tp / (tp + fn)
    tnr = tn / (tn + fp)
    ppv = tp / (tp + fp)
    npv = tn / (tn + fn)
    return tpr, tnr, ppv, npv
