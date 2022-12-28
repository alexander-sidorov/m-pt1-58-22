#include <iostream>
#include <map>


class Function {
public:
    virtual void operator() () = 0;
};


class CountCalls: public Function {
    static std::map<Function* const, int> *__calls;

    Function* const __inner;

public:
    explicit CountCalls(Function* const inner) : __inner(inner) {
        (*__calls)[__inner] = 0;
    }

    void operator()() {
        (*__inner)();
        ++((*__calls)[__inner]);
    }

    int nr_calls() {
        auto item = __calls->find(__inner);
        if (item == __calls->end()) {
            return 0;
        }

        return item->second;
    }
};

std::map<Function* const, int> *CountCalls::__calls = new std::map<Function* const, int>();

/* --------------------------------------------------- */


class HelloWorld: public Function {
public:
    void operator() () {
        std::cout << "Hello world!" << std::endl;
    }
};

class ByeBye: public Function {
public:
    void operator() () {
        std::cout << "Bye bye!" << std::endl;
    }
};


int main() {
    Function* helloworld = new HelloWorld();
    helloworld = new CountCalls(helloworld);

    Function* byebye = new ByeBye();
    byebye = new CountCalls(byebye);

    assert(dynamic_cast<CountCalls *>(helloworld)->nr_calls() == 0);
    assert(dynamic_cast<CountCalls *>(byebye)->nr_calls() == 0);

    (*helloworld)();
    (*helloworld)();
    (*helloworld)();
    (*byebye)();
    (*byebye)();

    assert(dynamic_cast<CountCalls *>(helloworld)->nr_calls() == 3);
    assert(dynamic_cast<CountCalls *>(byebye)->nr_calls() == 2);
}
