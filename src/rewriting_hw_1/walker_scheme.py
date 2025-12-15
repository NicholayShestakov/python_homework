class WalkerScheme:
    def __init__(self, events_and_probabilities: list[tuple[str, int]]):
        if sum(probability[1] for probability in events_and_probabilities) != 1:
            raise Exception("Сумма вероятностей не равна 1.")
        self.table = self._get_table(events_and_probabilities)

    def _get_table(self, events_and_probabilities):
        """Генерирует таблицу Уолкера."""
        equal_probability = (
            1 / len(events_and_probabilities)
        )  # Переменная с вероятностью события, если бы все события были равновероятными.
        probabilities = {
            event: equal_probability for event, _ in events_and_probabilities
        }  # Словарь, где изначально все вероятности эквивалентны и меняются после донорства кого-то кому-то.
        how_many_added_for_event = {
            event: 0 for event, _ in events_and_probabilities
        }  # Для заполнения нерозданных отрезков в конце
        table = []
        global_barrier = 0

        for i in range(len(events_and_probabilities)):
            break_flag = False
            for donor_event, donor_probability in events_and_probabilities:
                if donor_probability < probabilities[donor_event]:
                    for (
                        recipient_event,
                        recipient_probability,
                    ) in events_and_probabilities:
                        if recipient_probability > probabilities[recipient_event]:
                            table.append(
                                (
                                    donor_event,
                                    recipient_event,
                                    global_barrier
                                    + equal_probability
                                    - probabilities[donor_event]
                                    + donor_probability,  # Подсчёт барьера, где к глобальному барьеру прибавляется остаток вероятности донора по модулю эквивалентной вероятности
                                )
                            )
                            global_barrier += equal_probability

                            how_many_added_for_event[recipient_event] += (
                                equal_probability
                                - probabilities[donor_event]
                                + donor_probability
                            )
                            how_many_added_for_event[donor_event] += (
                                probabilities[donor_event] - donor_probability
                            )

                            probabilities[recipient_event] += (
                                probabilities[donor_event] - donor_probability
                            )
                            probabilities[donor_event] = donor_probability

                            break_flag = True
                            break
                    if break_flag:
                        break
            else:  # Для оставшихся
                for event, probability in how_many_added_for_event.items():
                    print(how_many_added_for_event)
                    if probability < probabilities[event]:
                        global_barrier += equal_probability
                        table.append((event, event, global_barrier))
                        break

        return table


scheme = WalkerScheme([("A", 0.1), ("B", 0.5), ("C", 0.4)])

print(scheme.table)
