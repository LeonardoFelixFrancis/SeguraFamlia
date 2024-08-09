import { Component, OnInit, signal } from '@angular/core';
import { Router } from '@angular/router';
import {FormControl, FormsModule, ReactiveFormsModule, Validators} from '@angular/forms';
import {MatFormFieldModule} from '@angular/material/form-field';
import {MatInputModule} from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { PersonService } from '../../core/services/person.service';
import {MatCalendar, MatDatepickerModule} from '@angular/material/datepicker';
import {provideNativeDateAdapter} from '@angular/material/core';


@Component({
  selector: 'app-home',
  standalone: true,
  providers: [provideNativeDateAdapter()],
  imports:[MatFormFieldModule, MatInputModule, FormsModule, ReactiveFormsModule, MatButtonModule, MatDatepickerModule, MatCalendar],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent implements OnInit {

  
  profile_picture = signal('');
  name = new FormControl('', [Validators.required]);
  birthdate = new FormControl('', [Validators.required]);


  constructor(
    private router: Router, 
    private personService: PersonService
  ) { }

  ngOnInit(): void {
    this.personService.getCurrentUser().subscribe((data) => {
      this.profile_picture.set(`http://localhost:8000${data.profile_picture}`);
      this.name.setValue(data.name);
      this.birthdate.setValue(data.birthdate);
    });
  }

}
