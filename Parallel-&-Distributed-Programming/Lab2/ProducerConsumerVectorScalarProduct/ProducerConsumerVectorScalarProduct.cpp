// ProducerConsumerVectorScalarProduct.cpp : This file contains the 'main' function. Program execution begins and ends there.
/**
Computation of the scalar product of two vectors using two threads. 
The first thread (producer) computes the products of pairs of elements - one from each vector - and feeds the second thread. 
The second thread (consumer) sums up the products computed by the first one. 
The two threads are behind synchronized with a condition variable and a mutex. 
The consumer is cleared to use each product as soon as it is computed by the producer thread.
*/
/**
The producer uses a unique_lock to prepare each product, then notifies the consumer after each product and
waits for it to end the product addition , then it continues. 
*/
#include <iostream>
#include <thread>
#include <mutex>
#include <condition_variable>
#include <vector>
#include <limits>

std::vector<int> v1{ 22, 55, 420, 5 , 1 , 1};
std::vector<int> v2{ 2, 5, 4, 9 , 8, 10};
std::mutex result_mutex;
std::mutex com_mutex;
std::condition_variable condVar;
bool prod_ready = false;
int prod = 1;
int result = 0;


void printVector(std::vector<int> v) {
    for (int x : v) std::cout << x << " ";
    std::cout << std::endl;
}


void producer() {
    // this_thread::sleep_for(chrono::seconds(1));
    int i = 0;
    int n = (v1.size() < v2.size()) ? v1.size() : v2.size();
    while (i < n) {
        int local_prod = v1[i] * v2[i];
        {
            std::unique_lock<std::mutex> lck(com_mutex);
            prod = local_prod;
            prod_ready = true;
            condVar.notify_one();
            std::cout << "producer prod: " << prod << "\n";
            while (prod_ready) {
                condVar.wait(lck);
            }
            i++;
        }
    }
}

void consumer() {
    int i = 0;
    int n = (v1.size() < v2.size()) ? v1.size() : v2.size();
    while (i < n) {
        int local_prod = 0;
        {
            std::unique_lock<std::mutex> lck(com_mutex);
            while (!prod_ready) {
                condVar.wait(lck);
            }
            local_prod = prod;
            prod_ready = false;
            condVar.notify_one();
        }
        std::cout << "consumer received: " << local_prod << "\n";
        result_mutex.lock();
        result += local_prod;
        result_mutex.unlock();
        i++;
    }
}

void producer2() {
    int i = 0;
    int n = (v1.size() < v2.size()) ? v1.size() : v2.size();
    while (i < n) {
        while (prod_ready) {}
        prod = v1[i] * v2[i];
        prod_ready = true;
        i++;
    }
}

void consumer2() {
    int i = 0;
    int n = (v1.size() < v2.size()) ? v1.size() : v2.size();
    while (i < n) {
        while (!prod_ready) {}
        std::cout << result << " += " << prod << "\n";
        result += prod;
        prod_ready = false;
        i++;
    }
}

int main()
{
    // cout << "Hello World!\n";
    std::thread t_prod(producer);
    std::thread t_cons(consumer);
   
    t_prod.join();
    t_cons.join();
    std::cout << "\nScalar product result: " << result << std::endl;
    return 0;
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
