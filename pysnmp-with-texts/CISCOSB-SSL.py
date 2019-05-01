#
# PySNMP MIB module CISCOSB-SSL (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCOSB-SSL
# Produced by pysmi-0.3.4 at Wed May  1 12:23:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, Integer32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, TimeTicks, Counter64, IpAddress, Bits, ModuleIdentity, ObjectIdentity, Counter32, iso, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Integer32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "TimeTicks", "Counter64", "IpAddress", "Bits", "ModuleIdentity", "ObjectIdentity", "Counter32", "iso", "Unsigned32")
TruthValue, RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "DisplayString", "TextualConvention")
rlSsl = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100))
rlSsl.setRevisions(('2003-09-21 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlSsl.setRevisionsDescriptions(('Added this MODULE-IDENTITY clause.',))
if mibBuilder.loadTexts: rlSsl.setLastUpdated('200309210000Z')
if mibBuilder.loadTexts: rlSsl.setOrganization('Cisco Small Business')
if mibBuilder.loadTexts: rlSsl.setContactInfo('Postal: 170 West Tasman Drive San Jose , CA 95134-1706 USA Website: Cisco Small Business Home http://www.cisco.com/smb>;, Cisco Small Business Support Community <http://www.cisco.com/go/smallbizsupport>')
if mibBuilder.loadTexts: rlSsl.setDescription('The private MIB module definition for SSL.')
rlSslCertificateGenerationTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 1), )
if mibBuilder.loadTexts: rlSslCertificateGenerationTable.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateGenerationTable.setDescription('This table is used for : 1. generating keys and self signed certificate - saved in flash and RAM (not in configuration file) 2. generating certificate requests - saved in RAM, can be read by rlSslCertificateExportTable 3. generating self signed certificate - saved in flash and RAM (not in configuraion file) By setting rlSslCertificateGenerationAction to the appropriate value this action takes place. The other fields of this table are used for each of this actions')
rlSslCertificateGenerationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 1, 1), ).setIndexNames((0, "CISCOSB-SSL", "rlSslCertificateGenerationIndex"))
if mibBuilder.loadTexts: rlSslCertificateGenerationEntry.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateGenerationEntry.setDescription(' The row definition for this table.')
rlSslCertificateGenerationIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 1, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateGenerationIndex.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateGenerationIndex.setDescription('This index is always set to 1 no matter for which certificate or certificate request the action refers to.')
rlSslCertificateGenerationId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateGenerationId.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateGenerationId.setDescription('The device can hold a number of keys/certificates/certificate requests. These certificates are always numbered from 1 to N (maximum number of certificates in device). This field decides to which keys/certificates/certificate requests the action refers.')
rlSslCertificateGenerationCountryName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateGenerationCountryName.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateGenerationCountryName.setDescription('Value of country name field that will appear when a new certificate request or self signed certificate is generated.')
rlSslCertificateGenerationStateOrProvinceName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateGenerationStateOrProvinceName.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateGenerationStateOrProvinceName.setDescription('Value of state or province name field that will appear when a new certificate or self signed certificate is generated.')
rlSslCertificateGenerationLocalityName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateGenerationLocalityName.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateGenerationLocalityName.setDescription('Value of locality field that will appear when a new certificate or self signed certificate is generated.')
rlSslCertificateGenerationOrganizationName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateGenerationOrganizationName.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateGenerationOrganizationName.setDescription('Value of organization field that will appear when a new certificate or self signed certificate is generated.')
rlSslCertificateGenerationOrganizationUnitName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateGenerationOrganizationUnitName.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateGenerationOrganizationUnitName.setDescription('Value of organization field that will appear when a new certificate or self signed certificate is generated.')
rlSslCertificateGenerationCommonName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateGenerationCommonName.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateGenerationCommonName.setDescription('Value of common name field that will appear when a new certificate or self signed certificate is generated.')
rlSslCertificateGenerationValidDays = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 1, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateGenerationValidDays.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateGenerationValidDays.setDescription("When generating self signed certificate this field sets the valid fields. 'Valid from' is current GMT and 'valid to' current GMT + the value of this field.")
rlSslCertificateGenerationRsaKeyLength = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(512, 2048))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateGenerationRsaKeyLength.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateGenerationRsaKeyLength.setDescription('Setting the RSA key size that will be created when a new key is generated - generateRsaKeyAndSelfSignedCertificate')
rlSslCertificateGenerationPassphrase = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 1, 1, 11), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateGenerationPassphrase.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateGenerationPassphrase.setDescription('When a RSA key is generated (generateRsaKeyAndSelfSignedCertificate) this passphrase is saved in flash and when the time comes and the certificate and the key are exported in PKCS12 format this passphrase is used to encrypt it. If the passphrase is empty the key and certificate can not be exported. There is no method of obtaining this passphrase once a key was generated.')
rlSslCertificateGenerationAction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("generateRsaKeyAndSelfSignedCertificate", 1), ("generateSelfSignedCertificate", 2), ("generatePkcs12", 3), ("generateCertificateRequest", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateGenerationAction.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateGenerationAction.setDescription('Setting to a regenerateCertificate causes a new certificate to be generated and to be used for all new sessions.')
rlSslCertificateExportTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 2), )
if mibBuilder.loadTexts: rlSslCertificateExportTable.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateExportTable.setDescription('This table is used for viewing saved data from RAM and flash.')
rlSslCertificateExportEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 2, 1), ).setIndexNames((0, "CISCOSB-SSL", "rlSslCertificateExportId"), (0, "CISCOSB-SSL", "rlSslCertificateExportType"), (0, "CISCOSB-SSL", "rlSslCertificateExportFragmentId"))
if mibBuilder.loadTexts: rlSslCertificateExportEntry.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateExportEntry.setDescription(' The row definition for this table.')
rlSslCertificateExportId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSslCertificateExportId.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateExportId.setDescription('Identifies the index of this certficate / certificate request the table holds.')
rlSslCertificateExportType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("certificateRequestPemFormat", 1), ("certificatePemFormat", 2), ("certificateOpenSslFormat", 3), ("certificateAndKeyPkcs12", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSslCertificateExportType.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateExportType.setDescription('Identifies the type of data the current entry shows.')
rlSslCertificateExportFragmentId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSslCertificateExportFragmentId.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateExportFragmentId.setDescription('Identifies the index of this fragment in the certificate request.')
rlSslCertificateExportFragmentText = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 2, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSslCertificateExportFragmentText.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateExportFragmentText.setDescription('A part of the readable text entry for the certificate request.')
rlSslCertificateSave = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateSave.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateSave.setDescription('Saves data from rlSslCertificateImportTable to RAM and CDB. When an external certificate should be copied to the device first we copy it to rlSslCertificateImportTable and then this scalar is set to the certificate id that we want to save - 1. All entries in rlSslCertificateImportTable that have this id and their format is equal to the current value of rlSslCertificateSaveFormat are concatenated. 2. If the imported certificate format is .. - section 1 result is validated against the key with the same index. If validation fails for any reason - the certificate is not saved and the setting this scalar fails.] This scalar is for certificate 1 only... for certificate 2 use rlSslCertificateSave2 ')
rlSslCertificateSaveFormat = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("x509", 1), ("pkcs12", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateSaveFormat.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateSaveFormat.setDescription('.')
rlSslImportedPKCS12CertificatePassphrase = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(8, 96))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslImportedPKCS12CertificatePassphrase.setStatus('current')
if mibBuilder.loadTexts: rlSslImportedPKCS12CertificatePassphrase.setDescription('.')
rlSslCertificateImportTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 6), )
if mibBuilder.loadTexts: rlSslCertificateImportTable.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateImportTable.setDescription('This table is used for copying an external certificate to the device - see rlSslCertificateSave')
rlSslCertificateImportEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 6, 1), ).setIndexNames((0, "CISCOSB-SSL", "rlSslCertificateImportId"), (0, "CISCOSB-SSL", "rlSslCertificateImportFormat"), (0, "CISCOSB-SSL", "rlSslCertificateImportFragmentId"))
if mibBuilder.loadTexts: rlSslCertificateImportEntry.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateImportEntry.setDescription(' The row definition for this table.')
rlSslCertificateImportId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 6, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateImportId.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateImportId.setDescription('The certificate ID.')
rlSslCertificateImportFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("x509", 1), ("pkcs12", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateImportFormat.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateImportFormat.setDescription('.')
rlSslCertificateImportFragmentId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 6, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateImportFragmentId.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateImportFragmentId.setDescription('Identifies the index of this fragment in the certificate.')
rlSslCertificateImportFragmentText = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 6, 1, 4), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateImportFragmentText.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateImportFragmentText.setDescription('A part of the readable text entry for the certificate.')
rlSslCertificateImportFragmentStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 6, 1, 5), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateImportFragmentStatus.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateImportFragmentStatus.setDescription('')
rlSslSSLv2Enable = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslSSLv2Enable.setStatus('current')
if mibBuilder.loadTexts: rlSslSSLv2Enable.setDescription("if enabled then SSLv2 will be supported , if disabled SSLv2 won't be supported. only SSLV3 and TSL1. Note: disabling SSLv2 is more secure.")
class RlSslPublicKeyAlgorithm(TextualConvention, Integer32):
    description = 'This textual convention describes the various possible public key algorithms. The key algorithm is used to select the PK to be generated and is also used when viewing the public keys.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("rsa", 1), ("dsa", 2))

rlSslImportExportSelfKeyTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 8), )
if mibBuilder.loadTexts: rlSslImportExportSelfKeyTable.setStatus('current')
if mibBuilder.loadTexts: rlSslImportExportSelfKeyTable.setDescription('This table can be used for 2 purposes: 1) Importing public/private key pair to serve as the device key when acting as SSL server. This is done by setting entries to this table, according to the specified format. When the last entry (footer) is set, the whole key pair is checked and if valid, stored in CDB. 2) Exporting the device SSL server public/private key. This can be done by performing GetNext operations on this table.')
rlSslImportExportSelfKeyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 8, 1), ).setIndexNames((0, "CISCOSB-SSL", "rlSslImportExportSelfKeyFormat"), (0, "CISCOSB-SSL", "rlSslImportExportSelfKeyIndex"), (0, "CISCOSB-SSL", "rlSslImportExportSelfKeyFragmentId"))
if mibBuilder.loadTexts: rlSslImportExportSelfKeyEntry.setStatus('current')
if mibBuilder.loadTexts: rlSslImportExportSelfKeyEntry.setDescription(' The row definition for this table.')
rlSslImportExportSelfKeyFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 8, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("uuencoded-format", 1))))
if mibBuilder.loadTexts: rlSslImportExportSelfKeyFormat.setStatus('current')
if mibBuilder.loadTexts: rlSslImportExportSelfKeyFormat.setDescription('Specifies the format of public/key pair. The following formats are supported for import/export: 1) uuencoded_format - in this format both private and public key are in uu-encoded format, and are seperated from one another by header and footer. An example of the concateneation of all fragments in this format is: -----BEGIN RSA PRIVATE KEY----- tDaNkZZoCxXfkLLsLDlZ6T9H8U4Gz637eRV7BYBpapkidAxY1UG0/qgfKLPkbId4wzht6ArV9bE4fMtX wSMOxL3q31pOmUdVhjbWYcgZQBDy1DjFSbuIEdP85c96B9bBE2nPv90mSvb/6j8R2NItT/KJeiYMtLtI N3m6/zESKJGIrX0jP1RFDjVZSS5chSAFgB0egsLZEyOQn7jAqpX/x/easD2J6F/OjPXlJ9Hff2tMb3NU QYyBoWH2J9IxhWB6Vo66R9Y04JGR18uL/rV2sMCtpg5ppkVTEpNTp9qE1yXocR2NmzUfNFap+GJ4IHj8 CzkVfmJM/kEWaJsYgHbAgLyRg4QVyelfobv1B71aQ+u1z9KGu/QajkWdR04OQfsGOL1CvU2LGYDcRjfH jv+jl/UkDRRjoD9kt2WvouT+OL6esvKl0OJBqWbGNXg9TWv/VLtJIwgUno+MLaJuOM4Fh44+wpnqUXwQ TFtBFc8pzt5BoOwbv9gXpicTkq4/+GhwXWXxSVFebKhnHAvKSLT+Ba7K7ZeR8EIIxbXdDNFOiS45R2KI jxxXLXK44u6KGl5MygCKXUOFlJ+Zhgrq6ZH17z/RVJQ2CWqb5Ekn9GY3kH9QZ3mb4MDPfriWi2lHGXHY JmJd4SLQhpBdnOS5tu84QmyU3dNbAdzghDsR+dEY/6g7Cn0kcVkeHNZ0H+mCZik5f6XBD8eplkk43bdR FrkwTeAjwurGcKwdiKkR4DlfSq3DKssVBucTqUpqsKqPXLwTIL44rWKhEPXgGPB2XDG0VLvIRKkAgEGI LNTwOm091Ro= -----END RSA PRIVATE KEY----- -----BEGIN RSA PUBLIC KEY----- MIGHAoGBAOeIC9gRg3YaEGGMp3C00qNwLINAEDZV/J4BWM5WnWwCWZyHXDs2XiEmFu0ZONAD4gcT2f2f NNfCBPye39VVuOkKQuSV0MLLX5800LZ4y1BNcPzPZHpnGaCzl7iAjhfj9MolzAh5VRjeiYt0t1um4dm+ q9A4BtfpJqDYxCW9uxd/AgEj -----END RSA PUBLIC KEY----- ')
rlSslImportExportSelfKeyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 8, 1, 2), Integer32())
if mibBuilder.loadTexts: rlSslImportExportSelfKeyIndex.setStatus('current')
if mibBuilder.loadTexts: rlSslImportExportSelfKeyIndex.setDescription('Identifies the SSL server key index (there can be more than one key).')
rlSslImportExportSelfKeyFragmentId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 8, 1, 3), Integer32())
if mibBuilder.loadTexts: rlSslImportExportSelfKeyFragmentId.setStatus('current')
if mibBuilder.loadTexts: rlSslImportExportSelfKeyFragmentId.setDescription('Identifies the index of this fragment in the key pair input/output.')
rlSslImportExportSelfKeyAlgorithm = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 8, 1, 4), RlSslPublicKeyAlgorithm()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslImportExportSelfKeyAlgorithm.setStatus('current')
if mibBuilder.loadTexts: rlSslImportExportSelfKeyAlgorithm.setDescription('Identifies the type of key pair.')
rlSslImportExportSelfKeyFragmentText = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 8, 1, 5), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslImportExportSelfKeyFragmentText.setStatus('current')
if mibBuilder.loadTexts: rlSslImportExportSelfKeyFragmentText.setDescription('A part of the readable text entry for the key pair input/output.')
rlSslCertificateSave2 = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateSave2.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateSave2.setDescription('Saves data from rlSslCertificateImportTable to RAM and CDB. When an external certificate should be copied to the device first we copy it to rlSslCertificateImportTable and then this scalar is set to the certificate id that we want to save - 1. All entries in rlSslCertificateImportTable that have this id and their format is equal to the current value of rlSslCertificateSaveFormat are concatenated. 2. If the imported certificate format is .. - section 1 result is validated against the key with the same index. If validation fails for any reason - the certificate is not saved and the setting this scalar fails.] This scalar is for certificate 2 only... for certificate 1 use rlSslCertificateSave ')
rlSslisCertificate1Default = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 10), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslisCertificate1Default.setStatus('current')
if mibBuilder.loadTexts: rlSslisCertificate1Default.setDescription('if set to true then this is the default key , will be configured when auto generation is done , will set to try , all other cases will be set to false. ')
rlSslisCertificate2Default = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100, 11), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslisCertificate2Default.setStatus('current')
if mibBuilder.loadTexts: rlSslisCertificate2Default.setDescription('if set to true then this is the default key , will be configured when auto generation is done , will set to try , all other cases will be set to false. ')
mibBuilder.exportSymbols("CISCOSB-SSL", rlSslImportExportSelfKeyEntry=rlSslImportExportSelfKeyEntry, rlSslisCertificate2Default=rlSslisCertificate2Default, rlSslCertificateExportFragmentText=rlSslCertificateExportFragmentText, rlSsl=rlSsl, rlSslCertificateGenerationStateOrProvinceName=rlSslCertificateGenerationStateOrProvinceName, rlSslCertificateSave=rlSslCertificateSave, rlSslCertificateGenerationCountryName=rlSslCertificateGenerationCountryName, rlSslCertificateGenerationId=rlSslCertificateGenerationId, rlSslImportedPKCS12CertificatePassphrase=rlSslImportedPKCS12CertificatePassphrase, rlSslImportExportSelfKeyAlgorithm=rlSslImportExportSelfKeyAlgorithm, rlSslCertificateGenerationLocalityName=rlSslCertificateGenerationLocalityName, rlSslCertificateGenerationValidDays=rlSslCertificateGenerationValidDays, rlSslCertificateExportEntry=rlSslCertificateExportEntry, rlSslCertificateGenerationRsaKeyLength=rlSslCertificateGenerationRsaKeyLength, rlSslCertificateImportId=rlSslCertificateImportId, rlSslCertificateGenerationIndex=rlSslCertificateGenerationIndex, rlSslCertificateSave2=rlSslCertificateSave2, rlSslCertificateGenerationCommonName=rlSslCertificateGenerationCommonName, rlSslCertificateImportEntry=rlSslCertificateImportEntry, rlSslCertificateGenerationTable=rlSslCertificateGenerationTable, rlSslCertificateImportTable=rlSslCertificateImportTable, rlSslCertificateImportFormat=rlSslCertificateImportFormat, rlSslCertificateGenerationEntry=rlSslCertificateGenerationEntry, rlSslCertificateImportFragmentText=rlSslCertificateImportFragmentText, rlSslCertificateSaveFormat=rlSslCertificateSaveFormat, rlSslCertificateImportFragmentStatus=rlSslCertificateImportFragmentStatus, rlSslImportExportSelfKeyTable=rlSslImportExportSelfKeyTable, RlSslPublicKeyAlgorithm=RlSslPublicKeyAlgorithm, rlSslSSLv2Enable=rlSslSSLv2Enable, rlSslImportExportSelfKeyFragmentText=rlSslImportExportSelfKeyFragmentText, rlSslCertificateGenerationOrganizationName=rlSslCertificateGenerationOrganizationName, rlSslImportExportSelfKeyIndex=rlSslImportExportSelfKeyIndex, rlSslCertificateExportFragmentId=rlSslCertificateExportFragmentId, rlSslImportExportSelfKeyFragmentId=rlSslImportExportSelfKeyFragmentId, rlSslCertificateExportType=rlSslCertificateExportType, rlSslCertificateGenerationOrganizationUnitName=rlSslCertificateGenerationOrganizationUnitName, rlSslCertificateGenerationAction=rlSslCertificateGenerationAction, rlSslCertificateExportId=rlSslCertificateExportId, PYSNMP_MODULE_ID=rlSsl, rlSslCertificateImportFragmentId=rlSslCertificateImportFragmentId, rlSslImportExportSelfKeyFormat=rlSslImportExportSelfKeyFormat, rlSslisCertificate1Default=rlSslisCertificate1Default, rlSslCertificateExportTable=rlSslCertificateExportTable, rlSslCertificateGenerationPassphrase=rlSslCertificateGenerationPassphrase)
