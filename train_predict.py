import os
import itertools
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import extract
import categorize

def Predict(file_name):
    label_list_path = os.path.join(os.path.dirname(__file__), "label_list")

    X_baseline_angle = []
    X_top_margin = []
    X_letter_size = []
    X_line_spacing = []
    X_word_spacing = []
    X_pen_pressure = []
    X_slant_angle = []
    y_t1 = []
    y_t2 = []
    y_t3 = []
    y_t4 = []
    y_t5 = []
    y_t6 = []
    y_t7 = []
    y_t8 = []
    page_ids = []


    print("Info: label_list found.")
    # =================================================================
    with open("label_list", "r") as labels:
        for line in labels:
            content = line.split()

            baseline_angle = float(content[0])
            X_baseline_angle.append(baseline_angle)

            top_margin = float(content[1])
            X_top_margin.append(top_margin)

            letter_size = float(content[2])
            X_letter_size.append(letter_size)

            line_spacing = float(content[3])
            X_line_spacing.append(line_spacing)

            word_spacing = float(content[4])
            X_word_spacing.append(word_spacing)

            pen_pressure = float(content[5])
            X_pen_pressure.append(pen_pressure)

            slant_angle = float(content[6])
            X_slant_angle.append(slant_angle)

            trait_1 = float(content[7])
            y_t1.append(trait_1)

            trait_2 = float(content[8])
            y_t2.append(trait_2)

            trait_3 = float(content[9])
            y_t3.append(trait_3)

            trait_4 = float(content[10])
            y_t4.append(trait_4)

            trait_5 = float(content[11])
            y_t5.append(trait_5)

            trait_6 = float(content[12])
            y_t6.append(trait_6)

            trait_7 = float(content[13])
            y_t7.append(trait_7)

            trait_8 = float(content[14])
            y_t8.append(trait_8)

            page_id = content[15]
            page_ids.append(page_id)
    # ===============================================================

    # emotional stability
    X_t1 = []
    for a, b in zip(X_baseline_angle, X_slant_angle):
        X_t1.append([a, b])

    # mental energy or will power
    X_t2 = []
    for a, b in zip(X_baseline_angle, X_slant_angle):
        X_t2.append([a, b])

    # modesty
    X_t3 = []
    for a, b in zip(X_baseline_angle, X_slant_angle):
        X_t3.append([a, b])

    # personal harmony and flexibility
    X_t4 = []
    for a, b in zip(X_baseline_angle, X_slant_angle):
        X_t4.append([a, b])

    # lack of discipline
    X_t5 = []
    for a, b in zip(X_baseline_angle, X_slant_angle):
        X_t5.append([a, b])

    # poor concentration
    X_t6 = []
    for a, b in zip(X_baseline_angle, X_slant_angle):
        X_t6.append([a, b])

    # non communicativeness
    X_t7 = []
    for a, b in zip(X_baseline_angle, X_slant_angle):
        X_t7.append([a, b])

    # social isolation
    X_t8 = []
    for a, b in zip(X_baseline_angle, X_slant_angle):
        X_t8.append([a, b])

    # print X_t1
    # print type(X_t1)
    # print len(X_t1)

    f = open('data.txt', 'w')
    X_train, X_test, y_train, y_test = train_test_split(
        X_t1, y_t1, test_size=.30, random_state=8)
    clf1 = SVC(kernel='rbf')
    clf1.fit(X_train, y_train)
    accuracy1 = accuracy_score(clf1.predict(X_test), y_test)
    print("Classifier 1 accuracy:", accuracy1)
    f.write(f"Classifier 1 accuracy:{accuracy1}\n")

    X_train, X_test, y_train, y_test = train_test_split(
        X_t2, y_t2, test_size=.30, random_state=16)
    clf2 = SVC(kernel='rbf')
    clf2.fit(X_train, y_train)
    accuracy2 = accuracy_score(clf1.predict(X_test), y_test)
    print("Classifier 2 accuracy:", accuracy1)
    f.write(f"Classifier 2 accuracy:{accuracy1}\n")

    X_train, X_test, y_train, y_test = train_test_split(
        X_t3, y_t3, test_size=.30, random_state=32)
    clf3 = SVC(kernel='rbf')
    clf3.fit(X_train, y_train)
    accuracy3= accuracy_score(clf1.predict(X_test), y_test)
    print("Classifier 3 accuracy:", accuracy1)
    f.write(f"Classifier 3 accuracy:{accuracy1}\n")

    X_train, X_test, y_train, y_test = train_test_split(
        X_t4, y_t4, test_size=.30, random_state=64)
    clf4 = SVC(kernel='rbf')
    clf4.fit(X_train, y_train)
    accuracy4 = accuracy_score(clf1.predict(X_test), y_test)
    print("Classifier 4 accuracy:", accuracy1)
    f.write(f"Classifier 4 accuracy:{accuracy1}\n")

    X_train, X_test, y_train, y_test = train_test_split(
        X_t5, y_t5, test_size=.30, random_state=42)
    clf5 = SVC(kernel='rbf')
    clf5.fit(X_train, y_train)
    accuracy5 = accuracy_score(clf1.predict(X_test), y_test)
    print("Classifier 5 accuracy:", accuracy1)
    f.write(f"Classifier 5 accuracy:{accuracy1}\n")

    X_train, X_test, y_train, y_test = train_test_split(
        X_t6, y_t6, test_size=.30, random_state=52)
    clf6 = SVC(kernel='rbf')
    clf6.fit(X_train, y_train)
    accuracy6 = accuracy_score(clf1.predict(X_test), y_test)
    print("Classifier 6 accuracy:", accuracy1)
    f.write(f"Classifier 6 accuracy:{accuracy1}\n")

    X_train, X_test, y_train, y_test = train_test_split(
        X_t7, y_t7, test_size=.30, random_state=21)
    clf7 = SVC(kernel='rbf')
    clf7.fit(X_train, y_train)
    accuracy7 = accuracy_score(clf1.predict(X_test), y_test)
    print("Classifier 7 accuracy:", accuracy1)
    f.write(f"Classifier 7 accuracy:{accuracy1}\n")

    X_train, X_test, y_train, y_test = train_test_split(
        X_t8, y_t8, test_size=.30, random_state=73)
    clf8 = SVC(kernel='rbf')
    clf8.fit(X_train, y_train)
    accuracy8 = accuracy_score(clf1.predict(X_test), y_test)
    print("Classifier 8 accuracy:", accuracy1)
    f.write(f"Classifier 8 accuracy:{accuracy1}\n")

    raw_features = extract.start(file_name)

    raw_baseline_angle = raw_features[0]
    baseline_angle, comment = categorize.determine_baseline_angle(raw_baseline_angle)
    print("Baseline Angle:", comment)
    f.write(f"Baseline Angle:{comment}\n")

    raw_top_margin = raw_features[1]
    top_margin, comment = categorize.determine_top_margin(raw_top_margin)
    print("Top Margin:", comment)
    f.write(f"Top Margin:{comment}\n")

    raw_letter_size = raw_features[2]
    letter_size, comment = categorize.determine_letter_size(raw_letter_size)
    print("Letter Size:", comment)
    f.write(f"Letter Size:{comment}\n")

    raw_line_spacing = raw_features[3]
    line_spacing, comment = categorize.determine_line_spacing(raw_line_spacing)
    print("Line Spacing:", comment)
    f.write(f"Line Spacing:{comment}\n")

    raw_word_spacing = raw_features[4]
    word_spacing, comment = categorize.determine_word_spacing(raw_word_spacing)
    print("Word Spacing:", comment)
    f.write(f"Word Spacing:{comment}\n")

    raw_pen_pressure = raw_features[5]
    pen_pressure, comment = categorize.determine_pen_pressure(raw_pen_pressure)
    print("Pen Pressure:", comment)
    f.write(f"Pen Pressure:{comment}\n")

    raw_slant_angle = raw_features[6]
    slant_angle, comment = categorize.determine_slant_angle(raw_slant_angle)
    print("Slant:", comment)
    f.write(f"Slant:{comment}\n")

    print("Emotional Stability:", clf1.predict([[baseline_angle, slant_angle]]))
    f.write("Emotional Stability:{}\n".format(clf1.predict([[baseline_angle, slant_angle]])))

    print("Mental Energy or Will Power:", clf2.predict([[letter_size, pen_pressure]]))
    f.write("Mental Energy or Will Power:{}\n".format(clf2.predict([[letter_size, pen_pressure]])))

    print("Modesty:", clf3.predict([[letter_size, top_margin]]))
    f.write("Modesty:{}\n".format(clf3.predict([[letter_size, top_margin]])))

    print("Personal Harmony and Flexibility:", clf4.predict([[line_spacing, word_spacing]]))
    f.write("Personal Harmony and Flexibility:{}\n".format(clf4.predict([[line_spacing, word_spacing]])))

    print("Lack of Discipline:", clf5.predict([[slant_angle, top_margin]]))
    f.write("Lack of Discipline:{}\n".format(clf5.predict([[slant_angle, top_margin]])))

    print("Poor Concentration:", clf6.predict([[letter_size, line_spacing]]))
    f.write("Poor Concentration:{}\n".format(clf6.predict([[letter_size, line_spacing]])))

    print("Non Communicativeness:", clf7.predict([[letter_size, word_spacing]]))
    f.write("Non Communicativeness:{}\n".format(clf7.predict([[letter_size, word_spacing]])))

    print("Social Isolation:", clf8.predict([[line_spacing, word_spacing]]))
    f.write("Social Isolation:{}\n".format(clf8.predict([[line_spacing, word_spacing]])))
    f.close()
    print("---------------------------------------------------")