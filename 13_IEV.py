def expect(dataset):
    num_couple = dataset.split(' ')

    prob_of_dom = [1, 1, 1, 0.75, 0.5, 0]

    E_1 = 0
    for k, p in zip(num_couple, prob_of_dom):
        E_1 += int(k) * p

    print(E_1 * 2)

expect('17584 19895 18601 18904 16727 17172')