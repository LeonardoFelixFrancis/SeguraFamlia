import { Person } from "./person_model";

export interface Family {
    id : number | null;
    surname : string | null;
    address : string | null;
    members : Person[] | null;
    phone_number : string | null;
}