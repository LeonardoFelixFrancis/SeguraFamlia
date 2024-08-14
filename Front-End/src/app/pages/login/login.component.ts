import {ChangeDetectionStrategy, Component, OnInit, signal} from '@angular/core';
import {takeUntilDestroyed} from '@angular/core/rxjs-interop';
import {FormControl, FormsModule, ReactiveFormsModule, Validators} from '@angular/forms';
import {MatFormFieldModule} from '@angular/material/form-field';
import {MatInputModule} from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { Router, RouterLink } from '@angular/router';
import {merge} from 'rxjs';
import {LoginService} from '../../core/services/login.service';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [MatFormFieldModule, MatInputModule, FormsModule, ReactiveFormsModule, MatButtonModule, RouterLink],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent implements OnInit {

  username = new FormControl('', [Validators.required]);
  password = new FormControl('', [Validators.required]);

  usernameErrorMessage = signal('');
  passwordErrorMessage = signal('');

  ngOnInit(): void {
    localStorage.removeItem('token');
  }

  constructor(
    private loginService: LoginService,
    private router: Router
  ) {
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
    
    if (this.username.invalid || this.password.invalid) {
      return;
    }

    this.loginService.login({
      username: this.username.value,
      password: this.password.value
    }).subscribe(
      (response) => {
        localStorage.setItem('token', response.access);
        this.router.navigate(['/home']);
      },
      (error) => {
        console.error('Error logging in', error);
      }
    );

  }

}
