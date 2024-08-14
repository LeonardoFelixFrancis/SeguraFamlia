import { Component, OnInit, Renderer2, signal, WritableSignal } from '@angular/core';
import { Router } from '@angular/router';
import {FormControl, FormsModule, ReactiveFormsModule, Validators} from '@angular/forms';
import {MatFormFieldModule} from '@angular/material/form-field';
import {MatInputModule} from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { PersonService } from '../../core/services/person.service';
import {MatCalendar, MatDatepickerModule} from '@angular/material/datepicker';
import {MAT_DATE_LOCALE} from '@angular/material/core';
import {provideMomentDateAdapter} from '@angular/material-moment-adapter';
import {MatIconModule} from '@angular/material/icon';
import { DatePipe } from '@angular/common';
import { DateTimeUtils } from '../../core/utils/date_time_utils';
import { Family } from '../../core/models/family_model';
import { MatDialog } from '@angular/material/dialog';
import { CreateFamilyComponent } from '../../dialogs/create-family/create-family.component';
import { MatDialogConfig } from '@angular/material/dialog';

@Component({
  selector: 'app-home',
  standalone: true,
  providers: [
    {provide: MAT_DATE_LOCALE, useValue: 'en-US'},
    provideMomentDateAdapter()],
  imports:[MatFormFieldModule, MatInputModule, FormsModule, ReactiveFormsModule, MatButtonModule, MatDatepickerModule, MatCalendar, MatIconModule, DatePipe],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent implements OnInit {

  is_editing:boolean = false;

  profile_picture = signal('');

  user_family:WritableSignal<Family> = signal<Family>({
    id:null,
    surname: null,
    members: null,
    address: null,
    phone_number: null
  });

  name = new FormControl('', [Validators.required]);
  birthdate = new FormControl('', [Validators.required]);
  profile_picture_form = new FormControl('');

  constructor(
    private router: Router, 
    private personService: PersonService,
    private dialogRef: MatDialog
  ) { }

  ngOnInit(): void {
    this.personService.getCurrentUser().subscribe((data) => {
      this.profile_picture.set(`http://localhost:8000${data.profile_picture}`);
      this.name.setValue(data.name);
      this.birthdate.setValue(data.birthdate);
    });
  }

  save(){

    if (this.name.invalid || this.birthdate.invalid) {
      return;
    }
    
    let date = null;
    if (this.birthdate.value !== null){
      date = new Date(this.birthdate.value);
      date = date.toLocaleDateString('en-US');
    }
    
    this.personService.update({
      name: this.name.value,
      birthdate: date,
      profile_picture: this.profile_picture_form.value
    }).subscribe(() => {
      this.changeEditState();
    });
  }

  changeEditState() {
    this.is_editing = !this.is_editing;
  }

  openImagePicker(){

    let input = document.getElementById('image-piccker') as HTMLInputElement;
    input.click();

    this.changeEditState();

  }

  onFileChange(event:any) {

    const file = event.target.files[0];

    const reader = new FileReader();

    

    reader.onloadend = () => {
      const base64String = reader.result as string;
      this.profile_picture_form.setValue(base64String);
      
    }
    reader.readAsDataURL(file);

    if (file) {
      this.profile_picture.set(URL.createObjectURL(file));
    }

  }

  create_family(){
    const dialogRef = this.dialogRef.open(CreateFamilyComponent);
  }

}
