import {ChangeDetectionStrategy, Component, signal} from '@angular/core';
import {takeUntilDestroyed} from '@angular/core/rxjs-interop';
import {FormControl, FormsModule, ReactiveFormsModule, Validators} from '@angular/forms';
import {MatFormFieldModule} from '@angular/material/form-field';
import {MatInputModule} from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { Router, RouterLink } from '@angular/router';
import {merge} from 'rxjs';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [MatFormFieldModule, MatInputModule, FormsModule, ReactiveFormsModule, MatButtonModule, RouterLink],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {

  username = new FormControl('', [Validators.required]);
  password = new FormControl('', [Validators.required]);

  usernameErrorMessage = signal('');
  passwordErrorMessage = signal('');
  
  constructor() {
    merge(this.username.statusChanges, this.username.valueChanges)
      .pipe(takeUntilDestroyed())
      .subscribe(() => this.updateErrorMessage());
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

  }

  login() {
    if (this.username.valid && this.password.valid) {
      console.log('Login successful');
    }
  }

}
