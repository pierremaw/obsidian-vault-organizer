**OAuth**: An open standard for access delegation, allowing users to grant third-party applications access to their resources without sharing credentials.

1. **Overview**
   * **Purpose**: Securely authorize third-party applications to access resources on behalf of users
   * **Origin**: Developed in 2006, OAuth 1.0 released in 2010
   * **Current version**: OAuth 2.0, released in 2012
   * **Widely adopted**: Used by major platforms such as Google, Facebook, and Twitter

2. **Core Concepts**
   * **Resource Owner**: The user who owns the resource being accessed
   * **Client**: The third-party application requesting access to the resource
   * **Resource Server**: The server hosting the protected resource
   * **Authorization Server**: The server responsible for granting access tokens

3. **OAuth 2.0 Grant Types**
   * **Authorization Code**: Used by web applications, requires user interaction
      * **Redirect**: User is redirected to the authorization server
      * **Consent**: User authorizes the client to access their resources
      * **Authorization Code**: Client receives a temporary code after successful authorization
      * **Access Token**: Client exchanges the authorization code for an access token
   * **Implicit**: Used by client-side applications, simplified version of Authorization Code
   * **Client Credentials**: Used by server-to-server applications, no user interaction required
   * **Resource Owner Password Credentials**: Used when the client is highly trusted, requires user credentials

4. **Access Tokens**
   * **Bearer Tokens**: The most common type, used to access resources without additional proof
   * **JWT (JSON Web Tokens)**: A compact, URL-safe token format containing claims and metadata
   * **Token Expiration**: Access tokens have a limited lifetime, requiring periodic refresh

5. **Security Considerations**
   * **HTTPS**: Use encrypted connections to prevent eavesdropping and man-in-the-middle attacks
   * **Client Authentication**: Verify the identity of the client using client ID and secret
   * **Redirect URI**: Validate the redirect URI to prevent unauthorized redirection
   * **Token Storage**: Securely store tokens to prevent unauthorized access

6. **Use Cases**
   * **Single Sign-On (SSO)**: Allow users to log in to multiple services using a single identity
   * **Third-Party Integrations**: Grant applications access to user data or services without sharing credentials
   * **API Access**: Control access to protected API endpoints using OAuth tokens

7. **Libraries and Frameworks**
   * **OAuth 2.0 Servers**: Various server implementations for different languages and platforms
      * **OAuth2 Server (Node.js)**: A popular OAuth 2.0 server for Node.js
      * **Doorkeeper (Ruby on Rails)**: A Ruby on Rails OAuth 2.0 server
      * **Spring Security OAuth (Java)**: A Java OAuth 2.0 server using the Spring framework
   * **OAuth 2.0 Clients**: Libraries for implementing OAuth 2.0 clients
      * **OAuth2 (Python)**: A Python OAuth 2.0 client library
      * **omniauth-oauth2 (Ruby)**: A Ruby OAuth 2.0 client using the OmniAuth framework
      * **AppAuth (iOS and Android)**: OAuth 2.0 clients for native mobile applications

8. **Resources**
   * **Official website**: [oauth.net](https://oauth.net/)
   * **Specification**: [RFC 6749 - The OAuth 2.0 Authorization Framework](https://tools.ietf.org/html/rfc6749)

___
Type: #subtopic 
Topics: [[Computer Science]], [[Software development]]

