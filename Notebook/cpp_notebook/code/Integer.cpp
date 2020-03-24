#include "Integer.h"

Integer::Integer() : _value(0)    // 调用默认构造时，会为私有成员变量 _value 初始化赋值为 0
{

}

// 重载+运算符
Integer Integer::operator+(Integer other){
    Integer result(this->_value + other._value);    // 用来返回的结果对象
    return result;
}

// 重载-运算符
const Integer Integer::operator-(const Integer & other) const{
    return Integer(this->_value - other._value);
}

// 重载赋值运算符
const Integer & Integer::operator=(const Integer & other) {
    // 条款11：如果是自我赋值，就不要做任何事情， 更加有效率
    // int4 = int4;
    if (this == &other) return *this;    // 证同测试
    this->_value = other._value;
    return *this;
}

Integer::~Integer()
{

}