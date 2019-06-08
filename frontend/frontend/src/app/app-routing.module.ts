import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { RegisterComponent } from './register/register.component';
import { ViewusersComponent } from './viewusers/viewusers.component';
import { HomeComponent } from './home/home.component';

const routes: Routes = [
{ path: 'register', component: RegisterComponent },
{ path: 'view',      component: ViewusersComponent },
{
  path: 'home',
  component: HomeComponent
},
{ path: '',
  redirectTo: '/home',
  pathMatch: 'full'
}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
