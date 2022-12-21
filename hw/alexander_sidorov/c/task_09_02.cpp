#include <iostream>
#include <map>


class CountCalls {
    static std::map<void (*)(), int> *our_calls_counter;

    void (*my_original_func)();

public:
    explicit CountCalls(void (*func)()) : my_original_func(func) {
        (*our_calls_counter)[func] = 0;
    }

    void operator()() {
        this->my_original_func();
        ++(*our_calls_counter)[this->my_original_func];
    }

    int nr_calls() {
        auto item = our_calls_counter->find(my_original_func);
        if (item == our_calls_counter->end()) {
            return 0;
        }

        return item->second;
    }
};

std::map<void (*)(), int> *CountCalls::our_calls_counter = new std::map<void (*)(), int>();

/* --------------------------------------------------- */

void helloworld_() {
    std::cout << "Hello world!" << std::endl;
}

CountCalls helloworld(helloworld_);


void byebye_() {
    std::cout << "Bye bye!!" << std::endl;
}

CountCalls byebye(byebye_);


int main() {
    assert(helloworld.nr_calls() == 0);
    assert(byebye.nr_calls() == 0);

    helloworld();
    helloworld();
    helloworld();
    byebye();
    byebye();

    assert(helloworld.nr_calls() == 3);
    assert(byebye.nr_calls() == 2);
}
