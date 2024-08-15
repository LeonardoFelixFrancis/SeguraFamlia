import { Component, inject,  } from '@angular/core';
import { FormsModule, FormControl, ReactiveFormsModule } from '@angular/forms';
import { MatButtonModule } from '@angular/material/button';
import { MatDialogActions, MatDialogClose, MatDialogTitle, MatDialogContainer, MatDialogModule, MatDialogContent, MatDialogRef } from '@angular/material/dialog';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { FamilyService } from '../../core/services/family.service';

@Component({
  selector: 'app-create-family',
  standalone: true,
  imports: [
    MatFormFieldModule,
    MatInputModule,
    FormsModule,
    ReactiveFormsModule,
    MatButtonModule,
    MatDialogTitle,
    MatDialogContent,
    MatDialogActions,
    MatDialogClose,
  ],
  templateUrl: './create-family.component.html',
  styleUrl: './create-family.component.css'
})
export class CreateFamilyComponent {

  readonly dialogRef = inject(MatDialogRef<CreateFamilyComponent>);
  readonly family_service = inject(FamilyService);

  family_name = new FormControl('');
  address = new FormControl('');
  phone_number = new FormControl('');

  cancel() {
    this.dialogRef.close();
  }

  save(){
    this.family_service.create({
      id: null,
      surname: this.family_name.value,
      members: null,
      address: this.address.value,
      phone_number: this.phone_number.value
    }).subscribe(() => {
      this.dialogRef.close();
    });
  }

}
