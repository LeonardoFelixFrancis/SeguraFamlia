class DateTimeUtils {
  static formatDate(date: string): string {
    return date.split('T')[0];
  }

  static formatTime(date: Date): string {
    return date.toISOString().split('T')[1].split('.')[0];
  }
}

export { DateTimeUtils };