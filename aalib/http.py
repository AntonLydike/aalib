from enum import IntEnum


class Status(IntEnum):
    # 200
    OK = 200
    Created = 201
    Accepted = 202
    NoContent = 204
    ResetContent = 205
    PartialContent = 206
    MultiStatus = 207
    AlreadyReported = 208

    # 300
    MultipleChoices = 300
    MovedPermanently = 301
    Found = 302
    SeeOther = 303
    NotModified = 304
    UseProxy = 305
    SwitchProxy = 306
    TemporaryRedirect = 307
    PermanentRedirect = 308

    # 400
    BadRequest = 400
    Unauthorized = 401
    PaymentRequired = 402
    Forbidden = 403
    NotFound = 404
    MethodNotAllowed = 405
    NotAcceptable = 406
    ProxyAuthenticationRequired = 407
    RequestTimeout = 408
    Conflict = 409
    Gone = 410
    LengthRequired = 411
    PreconditionFailed = 412
    RequestEntityTooLarge = 413
    RequestURITooLong = 414
    UnsupportedMediaType = 415
    RequestedRangeNotSatisfiable = 416
    ExpectationFailed = 417
    ImATeapot = 418
    AuthenticationTimeout = 419
    EnhanceYourCalm = 420
    UnprocessableEntity = 422
    Locked = 423
    FailedDependency = 424
    MethodFailure = 424
    UnorderedCollection = 425
    UpgradeRequired = 426
    PreconditionRequired = 428
    TooManyRequests = 429
    RequestHeaderFieldsTooLarge = 431
    NoResponse = 444
    RetryWith = 449
    BlockedByWindowsParentalControls = 450
    UnavailableForLegalReasons = 451
    Redirect = 451
    RequestHeaderTooLarge = 494
    CertError = 495
    NoCert = 496
    HTTPToHTTPS = 497
    ClientClosedRequest = 499

    # 500
    InternalServerError = 500
    NotImplemented = 501
    BadGateway = 502
    ServiceUnavailable = 503
    GatewayTimeout = 504
    HTTPVersionNotSupported = 505
    VariantAlsoNegotiates = 506
    InsufficientStorage = 507
    LoopDetected = 508
    BandwidthLimitExceeded = 509
    NotExtended = 510
    NetworkAuthenticationRequired = 511
    NetworkReadTimeoutError = 598
    NetworkConnectTimeoutError = 599

    @classmethod
    def from_code(cls, code: int):
        return cls(code)
