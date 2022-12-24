#include <iostream>

class DoTwice {
    void (*my_original_func)();

public:
    explicit DoTwice(void (*func)()) : my_original_func(func) {}

    void operator()() {
        this->my_original_func();
        this->my_original_func();
    }
};


void helloworld_() {
    std::cout << "Hello world!" << std::endl;
}

DoTwice helloworld(helloworld_);


int main() {
    helloworld();
}
