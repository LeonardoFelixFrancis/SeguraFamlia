import { HttpInterceptorFn } from '@angular/common/http';

export const bearerInterceptorInterceptor: HttpInterceptorFn = (req, next) => {
  const authToken = localStorage.getItem('token');

  // Clone the request and add the authorization header
  if (authToken) {
    const authReq = req.clone({
      setHeaders: {
        Authorization: "Bearer " + authToken
      }
    });

    // Pass the cloned request with the updated header to the next handler
    return next(authReq);
  }

  return next(req);

};