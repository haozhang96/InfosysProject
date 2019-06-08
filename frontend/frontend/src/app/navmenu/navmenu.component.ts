import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-navmenu',
  templateUrl: './navmenu.component.html',
  styleUrls: ['./navmenu.component.scss']
})
export class NavmenuComponent implements OnInit {

  navItems: any[] = [
    {
      name: 'Home',
      link: ''
    },
    {
      name: 'Register',
      link: '/register'
    },
    {
      name: 'View Users',
      link: '/view'
    }
  ];

  constructor() { }

  ngOnInit() {
  }

}
