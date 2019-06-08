import { Component, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';
@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit {
  nameFirst = new FormControl('');
  nameLast = new FormControl('');
  userName = new FormControl('');
  password = new FormControl('');
  email = new FormControl('');
  phone = new FormControl('');
  addressNameFirst = new FormControl('');
  addressNameLast = new FormControl('');
  addressStreet = new FormControl('');
  addressCity = new FormControl('');
  addressState = new FormControl('');
  addressZip = new FormControl('');
  creditCardNum = new FormControl('');
  creditCardCode = new FormControl('');
  creditCardExpire = new FormControl('');
  billingAddressNameFirst = new FormControl('');
  billingAddressNameLast = new FormControl('');
  billingAddressStreet = new FormControl('');
  billingAddressCity = new FormControl('');
  billingAddressState = new FormControl('');
  billingAddressZip = new FormControl('');

  constructor() { }

  ngOnInit() {
  }

  testClick() {
    let reqBody = {
      firstName: this.nameFirst.value,
      lastName: this.nameLast.value,
      userName: this.userName.value,
      password: this.password.value,
      email: this.email.value,
      phone: this.phone.value,
      homeAddress: {
        nameFirst: this.addressNameFirst.value,
        nameLast: this.addressNameLast.value,
        street: this.addressStreet.value,
        city: this.addressCity.value,
        state: this.addressState.value,
        zip: this.addressZip.value
      },
      billingCardNumber: this.creditCardNum.value,
      billingCardCode: this.creditCardCode.value,
      billingCardExpiration: this.creditCardExpire.value,
      billingAddress: {
      nameFirst: this.billingAddressNameFirst.value,
      nameLast: this.billingAddressNameLast.value,
      street: this.billingAddressStreet.value,
      city: this.billingAddressCity.value,
      state: this.billingAddressState.value,
      zip: this.billingAddressZip.value
      }
    };

    console.log(reqBody);
  }

}
