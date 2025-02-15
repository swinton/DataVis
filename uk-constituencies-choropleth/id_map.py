#!/usr/bin/env python

ID_MAP = dict([('513', 'South_East_Cornwall'),
 ('536', 'St_Austell_and_Newquay'),
 ('108', 'Camborne_and_Redruth'),
 ('583', 'Truro_and_Falmouth'),
 ('397', 'North_Cornwall'),
 ('539', 'St_Ives'),
 ('447', 'Plymouth_Moor_View'),
 ('393', 'Newton_Abbot'),
 ('221', 'Exeter'),
 ('122', 'Central_Devon'),
 ('575', 'Tiverton_and_Honiton'),
 ('398', 'North_Devon'),
 ('581', 'Totnes'),
 ('578', 'Torbay'),
 ('580', 'Torridge_and_West_Devon'),
 ('191', 'East_Devon'),
 ('448', 'Plymouth_Sutton_and_Devonport'),
 ('525', 'South_West_Devon'),
 ('647', 'Yeovil'),
 ('567', 'Taunton_Deane'),
 ('85', 'Bridgwater_and_West_Somerset'),
 ('505', 'Somerton_and_Frome'),
 ('609', 'Wells'),
 ('615', 'West_Dorset'),
 ('72', 'Bournemouth_East'),
 ('450', 'Poole'),
 ('73', 'Bournemouth_West'),
 ('362', 'Mid_Dorset_and_North_Poole'),
 ('138', 'Christchurch'),
 ('399', 'North_Dorset'),
 ('510', 'South_Dorset'),
 ('624', 'Weston-super-Mare'),
 ('412', 'North_Somerset'),
 ('92', 'Bristol_West'),
 ('91', 'Bristol_South'),
 ('89', 'Bristol_East'),
 ('408', 'North_East_Somerset'),
 ('227', 'Filton_and_Bradley_Stoke'),
 ('314', 'Kingswood'),
 ('573', 'Thornbury_and_Yate'),
 ('29', 'Bath'),
 ('90', 'Bristol_North_West'),
 ('485', 'Salisbury'),
 ('171', 'Devizes'),
 ('522', 'South_Swindon'),
 ('413', 'North_Swindon'),
 ('529', 'South_West_Wiltshire'),
 ('135', 'Chippenham'),
 ('422', 'North_Wiltshire'),
 ('130', 'Cheltenham'),
 ('569', 'Tewkesbury'),
 ('230', 'Forest_of_Dean'),
 ('557', 'Stroud'),
 ('246', 'Gloucester'),
 ('570', 'The_Cotswolds'),
 ('6', 'Aldershot'),
 ('406', 'North_East_Hampshire'),
 ('419', 'North_West_Hampshire'),
 ('27', 'Basingstoke'),
 ('272', 'Havant'),
 ('453', 'Portsmouth_South'),
 ('382', 'New_Forest_East'),
 ('383', 'New_Forest_West'),
 ('627', 'Winchester'),
 ('530', 'Southampton__Itchen'),
 ('531', 'Southampton__Test'),
 ('203', 'Eastleigh'),
 ('248', 'Gosport'),
 ('452', 'Portsmouth_North'),
 ('223', 'Fareham'),
 ('357', 'Meon_Valley'),
 ('194', 'East_Hampshire'),
 ('472', 'Romsey_and_Southampton_North'),
 ('300', 'Isle_of_Wight'),
 ('64', 'Bognor_Regis_and_Littlehampton'),
 ('641', 'Worthing_West'),
 ('200', 'East_Worthing_and_Shoreham'),
 ('14', 'Arundel_and_South_Downs'),
 ('364', 'Mid_Sussex'),
 ('289', 'Horsham'),
 ('155', 'Crawley'),
 ('133', 'Chichester'),
 ('291', 'Hove'),
 ('87', 'Brighton__Kemptown'),
 ('88', 'Brighton__Pavilion'),
 ('202', 'Eastbourne'),
 ('329', 'Lewes'),
 ('271', 'Hastings_and_Rye'),
 ('44', 'Bexhill_and_Battle'),
 ('606', 'Wealden'),
 ('619', 'West_Suffolk'),
 ('521', 'South_Suffolk'),
 ('103', 'Bury_St_Edmunds'),
 ('299', 'Ipswich'),
 ('558', 'Suffolk_Coastal'),
 ('123', 'Central_Suffolk_and_North_Ipswich'),
 ('605', 'Waveney'),
 ('93', 'Broadland'),
 ('410', 'North_Norfolk'),
 ('516', 'South_Norfolk'),
 ('527', 'South_West_Norfolk'),
 ('363', 'Mid_Norfolk'),
 ('426', 'Norwich_South'),
 ('425', 'Norwich_North'),
 ('253', 'Great_Yarmouth'),
 ('421', 'North_West_Norfolk'),
 ('70', 'Boston_and_Skegness'),
 ('344', 'Louth_and_Horncastle'),
 ('250', 'Grantham_and_Stamford'),
 ('502', 'Sleaford_and_North_Hykeham'),
 ('335', 'Lincoln'),
 ('233', 'Gainsborough'),
 ('514', 'South_Holland_and_the_Deepings'),
 ('252', 'Great_Grimsby'),
 ('143', 'Cleethorpes'),
 ('487', 'Scunthorpe'),
 ('313', 'Kingston-upon-Hull_West_and_Hessle'),
 ('311', 'Kingston-upon-Hull_East'),
 ('312', 'Kingston-upon-Hull_North'),
 ('260', 'Haltemprice_and_Howden'),
 ('43', 'Beverley_and_Holderness'),
 ('201', 'East_Yorkshire'),
 ('86', 'Brigg_and_Goole'),
 ('650', 'York_Outer'),
 ('490', 'Selby_and_Ainsty'),
 ('266', 'Harrogate_and_Knaresborough'),
 ('501', 'Skipton_and_Ripon'),
 ('572', 'Thirsk_and_Malton'),
 ('466', 'Richmond_Yorks'),
 ('486', 'Scarborough_and_Whitby'),
 ('649', 'York_Central'),
 ('547', 'Stockton_South'),
 ('368', 'Middlesbrough_South_and_East_Cleveland'),
 ('367', 'Middlesbrough'),
 ('461', 'Redcar'),
 ('546', 'Stockton_North'),
 ('269', 'Hartlepool'),
 ('56', 'Bishop_Auckland'),
 ('163', 'Darlington'),
 ('488', 'Sedgefield'),
 ('189', 'Easington'),
 ('401', 'North_Durham'),
 ('141', 'City_of_Durham'),
 ('418', 'North_West_Durham'),
 ('387', 'Newcastle-upon-Tyne_East'),
 ('290', 'Houghton_and_Sunderland_South'),
 ('603', 'Washington_and_Sunderland_West'),
 ('559', 'Sunderland_Central'),
 ('235', 'Gateshead'),
 ('62', 'Blaydon'),
 ('304', 'Jarrow'),
 ('519', 'South_Shields'),
 ('415', 'North_Tyneside'),
 ('586', 'Tynemouth'),
 ('386', 'Newcastle-upon-Tyne_Central'),
 ('388', 'Newcastle-upon-Tyne_North'),
 ('63', 'Blyth_Valley'),
 ('282', 'Hexham'),
 ('597', 'Wansbeck'),
 ('40', 'Berwick-upon-Tweed'),
 ('150', 'Copeland'),
 ('639', 'Workington'),
 ('444', 'Penrith_and_the_Border'),
 ('116', 'Carlisle'),
 ('623', 'Westmorland_and_Lonsdale'),
 ('25', 'Barrow_and_Furness'),
 ('99', 'Burnley'),
 ('442', 'Pendle'),
 ('618', 'West_Lancashire'),
 ('518', 'South_Ribble'),
 ('137', 'Chorley'),
 ('474', 'Rossendale_and_Darwen'),
 ('57', 'Blackburn'),
 ('294', 'Hyndburn'),
 ('465', 'Ribble_Valley'),
 ('60', 'Blackpool_South'),
 ('59', 'Blackpool_North_and_Cleveleys'),
 ('455', 'Preston'),
 ('232', 'Fylde'),
 ('644', 'Wyre_and_Preston_North'),
 ('319', 'Lancaster_and_Fleetwood'),
 ('377', 'Morecambe_and_Lunesdale'),
 ('234', 'Garston_and_Halewood'),
 ('339', 'Liverpool_Wavertree'),
 ('337', 'Liverpool_Riverside'),
 ('340', 'Liverpool_West_Derby'),
 ('338', 'Liverpool_Walton'),
 ('316', 'Knowsley'),
 ('538', 'St_Helens_South_and_Whiston'),
 ('537', 'St_Helens_North'),
 ('69', 'Bootle'),
 ('489', 'Sefton_Central'),
 ('533', 'Southport'),
 ('629', 'Wirral_South'),
 ('46', 'Birkenhead'),
 ('593', 'Wallasey'),
 ('630', 'Wirral_West'),
 ('328', 'Leigh'),
 ('351', 'Makerfield'),
 ('625', 'Wigan'),
 ('68', 'Bolton_West'),
 ('66', 'Bolton_North_East'),
 ('67', 'Bolton_South_East'),
 ('102', 'Bury_South'),
 ('101', 'Bury_North'),
 ('283', 'Heywood_and_Middleton'),
 ('468', 'Rochdale'),
 ('435', 'Oldham_West_and_Royton'),
 ('434', 'Oldham_East_and_Saddleworth'),
 ('484', 'Salford_and_Eccles'),
 ('640', 'Worsley_and_Eccles_South'),
 ('353', 'Manchester_Central'),
 ('58', 'Blackley_and_Broughton'),
 ('17', 'Ashton-under-Lyne'),
 ('542', 'Stalybridge_and_Hyde'),
 ('556', 'Stretford_and_Urmston'),
 ('355', 'Manchester_Withington'),
 ('354', 'Manchester_Gorton'),
 ('167', 'Denton_and_Reddish'),
 ('646', 'Wythenshawe_and_Sale_East'),
 ('8', 'Altrincham_and_Sale_West'),
 ('127', 'Cheadle'),
 ('545', 'Stockport'),
 ('274', 'Hazel_Grove'),
 ('261', 'Halton'),
 ('156', 'Crewe_and_Nantwich'),
 ('204', 'Eddisbury'),
 ('140', 'City_of_Chester'),
 ('211', 'Ellesmere_Port_and_Neston'),
 ('607', 'Weaver_Vale'),
 ('149', 'Congleton'),
 ('348', 'Macclesfield'),
 ('566', 'Tatton'),
 ('601', 'Warrington_South'),
 ('600', 'Warrington_North'),
 ('148', 'Colne_Valley'),
 ('292', 'Huddersfield'),
 ('172', 'Dewsbury'),
 ('30', 'Batley_and_Spen'),
 ('259', 'Halifax'),
 ('106', 'Calder_Valley'),
 ('76', 'Bradford_South'),
 ('77', 'Bradford_West'),
 ('75', 'Bradford_East'),
 ('498', 'Shipley'),
 ('305', 'Keighley'),
 ('324', 'Leeds_West'),
 ('456', 'Pudsey'),
 ('323', 'Leeds_North_West'),
 ('276', 'Hemsworth'),
 ('394', 'Normanton__Pontefract_and_Castleford'),
 ('592', 'Wakefield'),
 ('378', 'Morley_and_Outwood'),
 ('320', 'Leeds_Central'),
 ('321', 'Leeds_East'),
 ('322', 'Leeds_North_East'),
 ('212', 'Elmet_and_Rothwell'),
 ('496', 'Sheffield__Heeley'),
 ('492', 'Sheffield_Central'),
 ('493', 'Sheffield_South_East'),
 ('494', 'Sheffield__Brightside_and_Hillsborough'),
 ('495', 'Sheffield_Hallam'),
 ('443', 'Penistone_and_Stocksbridge'),
 ('475', 'Rother_Valley'),
 ('476', 'Rotherham'),
 ('611', 'Wentworth_and_Dearne'),
 ('24', 'Barnsley_East'),
 ('23', 'Barnsley_Central'),
 ('174', 'Doncaster_Central'),
 ('173', 'Don_Valley'),
 ('175', 'Doncaster_North'),
 ('199', 'East_Surrey'),
 ('217', 'Epsom_and_Ewell'),
 ('463', 'Reigate'),
 ('528', 'South_West_Surrey'),
 ('255', 'Guildford'),
 ('373', 'Mole_Valley'),
 ('220', 'Esher_and_Walton'),
 ('633', 'Woking'),
 ('560', 'Surrey_Heath'),
 ('479', 'Runnymede_and_Weybridge'),
 ('534', 'Spelthorne'),
 ('385', 'Newbury'),
 ('503', 'Slough'),
 ('74', 'Bracknell'),
 ('634', 'Wokingham'),
 ('628', 'Windsor'),
 ('460', 'Reading_West'),
 ('459', 'Reading_East'),
 ('349', 'Maidenhead'),
 ('278', 'Henley'),
 ('598', 'Wantage'),
 ('438', 'Oxford_East'),
 ('439', 'Oxford_West_and_Abingdon'),
 ('632', 'Witney'),
 ('20', 'Banbury'),
 ('32', 'Beaconsfield'),
 ('643', 'Wycombe'),
 ('131', 'Chesham_and_Amersham'),
 ('18', 'Aylesbury'),
 ('98', 'Buckingham'),
 ('371', 'Milton_Keynes_South'),
 ('370', 'Milton_Keynes_North'),
 ('500', 'Sittingbourne_and_Sheppey'),
 ('237', 'Gillingham_and_Rainham'),
 ('469', 'Rochester_and_Strood'),
 ('491', 'Sevenoaks'),
 ('251', 'Gravesham'),
 ('164', 'Dartford'),
 ('576', 'Tonbridge_and_Malling'),
 ('126', 'Chatham_and_Aylesford'),
 ('584', 'Tunbridge_Wells'),
 ('350', 'Maidstone_and_the_Weald'),
 ('224', 'Faversham_and_Mid-Kent'),
 ('16', 'Ashford'),
 ('111', 'Canterbury'),
 ('414', 'North_Thanet'),
 ('229', 'Folkestone_and_Hythe'),
 ('176', 'Dover'),
 ('523', 'South_Thanet'),
 ('483', 'Saffron_Walden'),
 ('147', 'Colchester'),
 ('142', 'Clacton'),
 ('270', 'Harwich_and_North_Essex'),
 ('78', 'Braintree'),
 ('216', 'Epping_Forest'),
 ('574', 'Thurrock'),
 ('532', 'Southend_West'),
 ('120', 'Castle_Point'),
 ('507', 'South_Basildon_and_East_Thurrock'),
 ('470', 'Rochford_and_Southend_East'),
 ('458', 'Rayleigh_and_Wickford'),
 ('26', 'Basildon_and_Billericay'),
 ('83', 'Brentwood_and_Ongar'),
 ('265', 'Harlow'),
 ('128', 'Chelmsford'),
 ('352', 'Maldon'),
 ('631', 'Witham'),
 ('228', 'Finchley_and_Golders_Green'),
 ('277', 'Hendon'),
 ('136', 'Chipping_Barnet'),
 ('295', 'Ilford_North'),
 ('210', 'Edmonton'),
 ('215', 'Enfield__Southgate'),
 ('214', 'Enfield_North'),
 ('273', 'Hayes_and_Harlington'),
 ('588', 'Uxbridge_and_South_Ruislip'),
 ('268', 'Harrow_West'),
 ('478', 'Ruislip__Northwood_and_Pinner'),
 ('267', 'Harrow_East'),
 ('263', 'Hampstead_and_Kilburn'),
 ('286', 'Holborn_and_St._Pancras'),
 ('80', 'Brent_Central'),
 ('81', 'Brent_North'),
 ('262', 'Hammersmith'),
 ('22', 'Barking'),
 ('162', 'Dagenham_and_Rainham'),
 ('471', 'Romford'),
 ('287', 'Hornchurch_and_Upminster'),
 ('617', 'West_Ham'),
 ('193', 'East_Ham'),
 ('451', 'Poplar_and_Limehouse'),
 ('42', 'Bethnal_Green_and_Bow'),
 ('139', 'Cities_of_London_and_Westminster'),
 ('622', 'Westminster_North'),
 ('129', 'Chelsea_and_Fulham'),
 ('307', 'Kensington'),
 ('585', 'Twickenham'),
 ('310', 'Kingston_and_Surbiton'),
 ('467', 'Richmond_Park'),
 ('437', 'Orpington'),
 ('33', 'Beckenham'),
 ('94', 'Bromley_and_Chislehurst'),
 ('331', 'Lewisham_West_and_Penge'),
 ('330', 'Lewisham_East'),
 ('332', 'Lewisham__Deptford'),
 ('159', 'Croydon_South'),
 ('157', 'Croydon_Central'),
 ('158', 'Croydon_North'),
 ('561', 'Sutton_and_Cheam'),
 ('119', 'Carshalton_and_Wallington'),
 ('372', 'Mitcham_and_Morden'),
 ('626', 'Wimbledon'),
 ('457', 'Putney'),
 ('577', 'Tooting'),
 ('31', 'Battersea'),
 ('179', 'Dulwich_and_West_Norwood'),
 ('555', 'Streatham'),
 ('591', 'Vauxhall'),
 ('107', 'Camberwell_and_Peckham'),
 ('39', 'Bermondsey_and_Old_Southwark'),
 ('433', 'Old_Bexley_and_Sidcup'),
 ('45', 'Bexleyheath_and_Crayford'),
 ('213', 'Eltham'),
 ('254', 'Greenwich_and_Woolwich'),
 ('219', 'Erith_and_Thamesmead'),
 ('225', 'Feltham_and_Heston'),
 ('82', 'Brentford_and_Isleworth'),
 ('296', 'Ilford_South'),
 ('333', 'Leyton_and_Wanstead'),
 ('596', 'Walthamstow'),
 ('134', 'Chingford_and_Woodford_Green'),
 ('582', 'Tottenham'),
 ('288', 'Hornsey_and_Wood_Green'),
 ('302', 'Islington_South_and_Finsbury'),
 ('301', 'Islington_North'),
 ('186', 'Ealing_Central_and_Acton'),
 ('188', 'Ealing__Southall'),
 ('187', 'Ealing_North'),
 ('257', 'Hackney_South_and_Shoreditch'),
 ('256', 'Hackney_North_and_Stoke_Newington'),
 ('293', 'Huntingdon'),
 ('109', 'Cambridge'),
 ('508', 'South_Cambridgeshire'),
 ('512', 'South_East_Cambridgeshire'),
 ('446', 'Peterborough'),
 ('417', 'North_West_Cambridgeshire'),
 ('403', 'North_East_Cambridgeshire'),
 ('535', 'St_Albans'),
 ('275', 'Hemel_Hempstead'),
 ('526', 'South_West_Hertfordshire'),
 ('604', 'Watford'),
 ('281', 'Hertsmere'),
 ('96', 'Broxbourne'),
 ('280', 'Hertford_and_Stortford'),
 ('610', 'Welwyn_Hatfield'),
 ('543', 'Stevenage'),
 ('285', 'Hitchin_and_Harpenden'),
 ('407', 'North_East_Hertfordshire'),
 ('347', 'Luton_South'),
 ('346', 'Luton_North'),
 ('524', 'South_West_Bedfordshire'),
 ('34', 'Bedford'),
 ('360', 'Mid_Bedfordshire'),
 ('402', 'North_East_Bedfordshire'),
 ('65', 'Bolsover'),
 ('132', 'Chesterfield'),
 ('404', 'North_East_Derbyshire'),
 ('509', 'South_Derbyshire'),
 ('218', 'Erewash'),
 ('169', 'Derby_South'),
 ('168', 'Derby_North'),
 ('361', 'Mid_Derbyshire'),
 ('10', 'Amber_Valley'),
 ('170', 'Derbyshire_Dales'),
 ('284', 'High_Peak'),
 ('97', 'Broxtowe'),
 ('15', 'Ashfield'),
 ('356', 'Mansfield'),
 ('429', 'Nottingham_South'),
 ('427', 'Nottingham_East'),
 ('428', 'Nottingham_North'),
 ('236', 'Gedling'),
 ('497', 'Sherwood'),
 ('480', 'Rushcliffe'),
 ('384', 'Newark'),
 ('28', 'Bassetlaw'),
 ('125', 'Charnwood'),
 ('343', 'Loughborough'),
 ('264', 'Harborough'),
 ('515', 'South_Leicestershire'),
 ('326', 'Leicester_South'),
 ('325', 'Leicester_East'),
 ('327', 'Leicester_West'),
 ('71', 'Bosworth'),
 ('420', 'North_West_Leicestershire'),
 ('482', 'Rutland_and_Melton'),
 ('424', 'Northampton_South'),
 ('423', 'Northampton_North'),
 ('608', 'Wellingborough'),
 ('308', 'Kettering'),
 ('151', 'Corby'),
 ('517', 'South_Northamptonshire'),
 ('165', 'Daventry'),
 ('279', 'Hereford_and_South_Herefordshire'),
 ('409', 'North_Herefordshire'),
 ('345', 'Ludlow'),
 ('499', 'Shrewsbury_and_Atcham'),
 ('568', 'Telford'),
 ('571', 'The_Wrekin'),
 ('411', 'North_Shropshire'),
 ('549', 'Stoke-on-Trent_North'),
 ('520', 'South_Staffordshire'),
 ('110', 'Cannock_Chase'),
 ('540', 'Stafford'),
 ('551', 'Stone'),
 ('565', 'Tamworth'),
 ('334', 'Lichfield'),
 ('100', 'Burton'),
 ('389', 'Newcastle-under-Lyme'),
 ('550', 'Stoke-on-Trent_South'),
 ('548', 'Stoke-on-Trent_Central'),
 ('541', 'Staffordshire_Moorlands'),
 ('95', 'Bromsgrove'),
 ('621', 'West_Worcestershire'),
 ('462', 'Redditch'),
 ('638', 'Worcester'),
 ('366', 'Mid_Worcestershire'),
 ('645', 'Wyre_Forest'),
 ('554', 'Stratford-on-Avon'),
 ('602', 'Warwick_and_Leamington'),
 ('306', 'Kenilworth_and_Southam'),
 ('477', 'Rugby'),
 ('430', 'Nuneaton'),
 ('416', 'North_Warwickshire'),
 ('154', 'Coventry_South'),
 ('152', 'Coventry_North_East'),
 ('153', 'Coventry_North_West'),
 ('504', 'Solihull'),
 ('358', 'Meriden'),
 ('52', 'Birmingham__Northfield'),
 ('54', 'Birmingham__Selly_Oak'),
 ('49', 'Birmingham__Hall_Green'),
 ('47', 'Birmingham__Edgbaston'),
 ('55', 'Birmingham__Yardley'),
 ('50', 'Birmingham__Hodge_Hill'),
 ('51', 'Birmingham__Ladywood'),
 ('48', 'Birmingham__Erdington'),
 ('53', 'Birmingham__Perry_Barr'),
 ('562', 'Sutton_Coldfield'),
 ('258', 'Halesowen_and_Rowley_Regis'),
 ('599', 'Warley'),
 ('613', 'West_Bromwich_East'),
 ('614', 'West_Bromwich_West'),
 ('552', 'Stourbridge'),
 ('178', 'Dudley_South'),
 ('177', 'Dudley_North'),
 ('636', 'Wolverhampton_South_East'),
 ('637', 'Wolverhampton_South_West'),
 ('635', 'Wolverhampton_North_East'),
 ('595', 'Walsall_South'),
 ('594', 'Walsall_North'),
 ('7', 'Aldridge-Brownhills'),
 ('13', 'Argyll_and_Bute'),
 ('298', 'Inverness__Nairn__Badenoch_and_Strathspey'),
 ('180', 'Dumfries_and_Galloway'),
 ('181', 'Dumfriesshire__Clydesdale_and_Tweeddale'),
 ('41', 'Berwickshire__Roxburgh_and_Selkirk'),
 ('184', 'Dunfermline_and_West_Fife'),
 ('315', 'Kirkcaldy_and_Cowdenbeath'),
 ('245', 'Glenrothes'),
 ('405', 'North_East_Fife'),
 ('431', 'Ochil_and_South_Perthshire'),
 ('19', 'Ayr__Carrick_and_Cumnock'),
 ('616', 'West_Dunbartonshire'),
 ('121', 'Central_Ayrshire'),
 ('197', 'East_Lothian'),
 ('369', 'Midlothian'),
 ('396', 'North_Ayrshire_and_Arran'),
 ('309', 'Kilmarnock_and_Loudoun'),
 ('297', 'Inverclyde'),
 ('336', 'Linlithgow_and_East_Falkirk'),
 ('208', 'Edinburgh_South_West'),
 ('207', 'Edinburgh_South'),
 ('205', 'Edinburgh_East'),
 ('206', 'Edinburgh_North_and_Leith'),
 ('209', 'Edinburgh_West'),
 ('341', 'Livingston'),
 ('441', 'Paisley_and_Renfrewshire_South'),
 ('195', 'East_Kilbride__Strathaven_and_Lesmahagow'),
 ('440', 'Paisley_and_Renfrewshire_North'),
 ('198', 'East_Renfrewshire'),
 ('318', 'Lanark_and_Hamilton_East'),
 ('379', 'Motherwell_and_Wishaw'),
 ('5', 'Airdrie_and_Shotts'),
 ('481', 'Rutherglen_and_Hamilton_West'),
 ('241', 'Glasgow_North_East'),
 ('244', 'Glasgow_South_West'),
 ('243', 'Glasgow_South'),
 ('238', 'Glasgow_Central'),
 ('239', 'Glasgow_East'),
 ('240', 'Glasgow_North'),
 ('242', 'Glasgow_North_West'),
 ('146', 'Coatbridge__Chryston_and_Bellshill'),
 ('192', 'East_Dunbartonshire'),
 ('160', 'Cumbernauld__Kilsyth_and_Kirkintilloch_East'),
 ('222', 'Falkirk'),
 ('544', 'Stirling'),
 ('445', 'Perth_and_North_Perthshire'),
 ('183', 'Dundee_West'),
 ('182', 'Dundee_East'),
 ('11', 'Angus'),
 ('4', 'Aberdeen_South'),
 ('3', 'Aberdeen_North'),
 ('612', 'West_Aberdeenshire_and_Kincardine'),
 ('247', 'Gordon'),
 ('21', 'Banff_and_Buchan'),
 ('376', 'Moray'),
 ('473', 'Ross__Skye_and_Lochaber'),
 ('105', 'Caithness__Sutherland_and_Easter_Ross'),
 ('380', 'Na_h-Eileanan_an_Iar'),
 ('454', 'Preseli_Pembrokeshire'),
 ('12', 'Arfon'),
 ('185', 'Dwyfor_Meirionnydd'),
 ('124', 'Ceredigion'),
 ('118', 'Carmarthen_West_and_South_Pembrokeshire'),
 ('342', 'Llanelli'),
 ('117', 'Carmarthen_East_And_Dinefwr'),
 ('2', 'Aberconwy'),
 ('1', 'Aberavon'),
 ('563', 'Swansea_East'),
 ('564', 'Swansea_West'),
 ('249', 'Gower'),
 ('381', 'Neath'),
 ('590', 'Vale_of_Glamorgan'),
 ('114', 'Cardiff_South_and_Penarth'),
 ('115', 'Cardiff_West'),
 ('112', 'Cardiff_Central'),
 ('113', 'Cardiff_North'),
 ('84', 'Bridgend'),
 ('432', 'Ogmore'),
 ('464', 'Rhondda'),
 ('449', 'Pontypridd'),
 ('391', 'Newport_West'),
 ('390', 'Newport_East'),
 ('161', 'Cynon_Valley'),
 ('61', 'Blaenau_Gwent'),
 ('104', 'Caerphilly'),
 ('303', 'Islwyn'),
 ('579', 'Torfaen'),
 ('359', 'Merthyr_Tydfil_and_Rhymney'),
 ('374', 'Monmouth'),
 ('79', 'Brecon_and_Radnorshire'),
 ('375', 'Montgomeryshire'),
 ('144', 'Clwyd_South'),
 ('145', 'Clwyd_West'),
 ('589', 'Vale_of_Clwyd'),
 ('166', 'Delyn'),
 ('642', 'Wrexham'),
 ('9', 'Alyn_and_Deeside'),
 ('648', 'Ynys_Mon'),
 ('392', 'Newry_and_Armagh'),
 ('620', 'West_Tyrone'),
 ('365', 'Mid_Ulster'),
 ('231', 'Foyle'),
 ('196', 'East_Londonderry'),
 ('587', 'Upper_Bann'),
 ('511', 'South_Down'),
 ('317', 'Lagan_Valley'),
 ('553', 'Strangford'),
 ('400', 'North_Down'),
 ('190', 'East_Antrim'),
 ('506', 'South_Antrim'),
 ('395', 'North_Antrim'),
 ('226', 'Fermanagh_and_South_Tyrone'),
 ('37', 'Belfast_South'),
 ('38', 'Belfast_West'),
 ('35', 'Belfast_East'),
 ('36', 'Belfast_North'),
 ('436', 'Orkney_and_Shetland')])