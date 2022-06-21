const faNumbers: any[] = ['۰','۱','۲','۳','۴','۵','۶','۷','۸','۹'];

const enToFa = (number: Number) => {
    let strNum = String(number);

    for(let i=0; i<strNum.length; i++){
        strNum = strNum.replace(strNum.charAt(i), faNumbers[i]);
    }

    return strNum;
}

const faToEn = (number: any) => {

    for(let i=0; i<number.length; i++){
        number = number.replace(number.charAt(i), faNumbers.indexOf(number.charAt(i)));
    }

    return number;
}