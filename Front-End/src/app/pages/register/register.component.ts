import {ChangeDetectionStrategy, Component, signal} from '@angular/core';
import {FormControl, FormsModule, ReactiveFormsModule, Validators} from '@angular/forms';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { RouterLink } from '@angular/router';
import {MatCalendar, MatDatepickerModule} from '@angular/material/datepicker';
import {provideNativeDateAdapter} from '@angular/material/core';

@Component({
  selector: 'app-register',
  standalone: true,
  providers: [provideNativeDateAdapter()],
  imports: [MatFormFieldModule, MatInputModule, FormsModule, ReactiveFormsModule, MatButtonModule, RouterLink, MatDatepickerModule, MatCalendar],
  templateUrl: './register.component.html',
  styleUrl: './register.component.css'
})
export class RegisterComponent {

  username = new FormControl('', [Validators.required]);
  password = new FormControl('', [Validators.required]);
  confirmPassword = new FormControl('', [Validators.required]);
  name = new FormControl('', [Validators.required]);
  age = new FormControl('', [Validators.required]);
  birthdate = new FormControl('', [Validators.required]);

  usernameErrorMessage = signal('');
  passwordErrorMessage = signal('');
  confirmPasswordErrorMessage = signal('');
  nameErrorMessage = signal('');
  ageErrorMessage = signal('');
  birthdateErrorMessage = signal('');

  constructor() {
    this.username.valueChanges.subscribe(() => this.updateErrorMessage());
    this.password.valueChanges.subscribe(() => this.updateErrorMessage());
    this.confirmPassword.valueChanges.subscribe(() => this.updateErrorMessage());
    this.name.valueChanges.subscribe(() => this.updateErrorMessage());
    this.age.valueChanges.subscribe(() => this.updateErrorMessage());
    this.birthdate.valueChanges.subscribe(() => this.updateErrorMessage());
  }

  updateErrorMessage() {
    if (this.username.hasError('required')) {
      this.usernameErrorMessage.set('You must enter a value');
    } else if (this.username.hasError('username')) {
      this.usernameErrorMessage.set('Not a valid username');
    } else {
      this.usernameErrorMessage.set('');
    }

    if (this.password.hasError('required')) {
      this.passwordErrorMessage.set('You must enter a value');
    } else {
      this.passwordErrorMessage.set('');
    }

    if (this.confirmPassword.hasError('required')) {
      this.confirmPasswordErrorMessage.set('You must enter a value');
    } else {
      this.confirmPasswordErrorMessage.set('');
    }

    if (this.name.hasError('required')) {
      this.nameErrorMessage.set('You must enter a value');
    } else {
      this.nameErrorMessage.set('');
    }

    if (this.age.hasError('required')) {
      this.ageErrorMessage.set('You must enter a value');
    } else {
      this.ageErrorMessage.set('');
    }

    if (this.birthdate.hasError('required')) {
      this.birthdateErrorMessage.set('You must enter a value');
    } else {
      this.birthdateErrorMessage.set('');
    }

  }

  register() {

    if (this.password.value !== this.confirmPassword.value) {
      this.confirmPassword.setErrors({passwordMatch: true});
      this.confirmPasswordErrorMessage.set('Passwords do not match');
    }

    if (this.username.valid && this.password.valid && this.confirmPassword.valid && this.name.valid && this.age.valid && this.birthdate.valid) {
      console.log('Register successful');
    }
  }


}
