"use strict";
const faNumbers = ['۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹'];
const enToFa = (number) => {
    let strNum = String(number);
    for (let i = 0; i < strNum.length; i++) {
        strNum = strNum.replace(strNum.charAt(i), faNumbers[i]);
    }
    return strNum;
};
const faToEn = (number) => {
    for (let i = 0; i < number.length; i++) {
        number = number.replace(number.charAt(i), faNumbers.indexOf(number.charAt(i)));
    }
    return number;
};
let lo = "۱۲۳";
console.log(faToEn(lo));
