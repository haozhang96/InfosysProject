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
    console.log(this.nameFirst, this.nameLast);
  }

}
