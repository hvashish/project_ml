from flask import *

from app import app
views = Blueprint('views', __name__)
@app.route('/')
@app.route('/index')
def index():
    return '<h1> Hello Mona!, I am going to create a first ML project<h1>'

@app.route('/NAS/BIGOS_DataFormat', methods=['GET', 'POST'])
def BIGOS_DataFormat():
	import pandas as pd
	import numpy as np
	import tempfile
	from app.forms import BIGOS_form
	form = BIGOS_form()
	if request.method == 'POST':
		if request.form['action'] == 'Import_Data':
			gsmcsv = request.files.get('gsmData')
			gsmData = pd.read_csv(gsmcsv)
			gsmData['bsic'] = gsmData['bsic'].astype(str)
			gsmData['bsic'] = gsmData['bsic'].str.zfill(2)
			gsmData[['ncc', 'bcc']] = gsmData['bsic'].astype(str).apply(lambda x: pd.Series(list(x))).astype(int,
																											 errors='ignore')
			gsm = gsmData[
				['siteid', 'cell', 'status', 'bcch', 'bsic', 'lac', 'ci', 'longitude', 'latitude', 'orientation', \
				 'tech', 'm_dtilts', 'e_dtilts', 'beam_width', 'mcc', 'mnc', 'ncc', 'bcc']]
			gsm["Total Tilt"] = gsm.apply(lambda row: row['m_dtilts': 'e_dtilts'].sum(), axis=1)
			gsm['band'] = 1900
			gsm['operator'] = 'T-Mobile'
			gsm.rename(columns={'siteid': 'H_sitename', 'cell': 'H_cellname', \
								'orientation': 'azimuth', 'm_dtilts': 'Mech. Downtilt', 'e_dtilts': 'Elec. Downtilt', \
								'beam_width': 'beamwidth', 'mcc': 'MCC', 'mnc': 'MNC'}, inplace=True)
			gsm[''] = ''
			GSMdata = gsm[['H_sitename', 'H_cellname', 'status', 'bcch', 'band', 'lac', 'ci', 'ncc', 'bcc', 'longitude', \
						   'latitude', 'azimuth', 'tech', \
						   'Mech. Downtilt', 'Elec. Downtilt', 'Total Tilt', 'beamwidth', '', 'MCC', 'MNC', 'operator']]

			# print(GSMdata)

			# elif request.form['action'] == 'Import_UMTS':
			umtscsv = request.files.get('umtsData')
			umtsData = pd.read_csv(umtscsv)
			umtsData['status'] = ''
			umtsData['band'] = ''
			# umtsData["Total Tilt"] = umtsData.apply(lambda row: row['dtilts_m' : 'ev_dtilts'].sum(),axis=1)
			umtsData["Total Tilt"] = umtsData[['dtilts_m', 'ev_dtilts']].sum(axis=1)
			umtsData['MCC'] = ''
			umtsData['MNC'] = ''
			umtsData['operator'] = 'T-Mobile'
			umtsData[''] = ''
			umtsData.rename(columns={'siteid': 'sitename', 'cell': 'cellname', 'uarfcndl': 'uarfcn', 'cid': 'ci',
									 'primaryscramblingcode': 'psc', \
									 'orientation': 'azimuth', 'dtilts_m': 'Mech. Downtilt',
									 'ev_dtilts': 'Elec. Downtilt', 'beam_width': 'beamwidth'}, inplace=True)
			UMTSData = umtsData[
				['sitename', 'cellname', 'uarfcn', 'status', 'band', 'rnc', 'lac', 'ci', 'psc', 'longitude', \
				 'latitude', 'azimuth', 'tech', 'Mech. Downtilt', 'Elec. Downtilt', 'Total Tilt', 'beamwidth', '',
				 'MCC', 'MNC', 'operator']]
			# print('umtsdata',UMTSData)
			# elif request.form['action'] == 'Import_LTE':
			ltecsv = request.files.get('lteData')
			lteData = pd.read_csv(ltecsv)
			lteData['operator'] = 'T-Mobile'
			lteData["Total Tilt"] = lteData[['m_dtilts', 'e_dtilts']].sum(axis=1)
			lteData[''] = ''
			lteData['band'] = ''
			lteData.rename(
				columns={'siteid': 'sitename', 'cell': 'cellname', 'dlearfcn': 'earfcndl', 'physicalcellid': 'pci', \
						 'orientation': 'azimuth', 'm_dtilts': 'Mech. Downtilt', 'e_dtilts': 'Elec. Downtilt',
						 'beam_width': 'beamwidth', \
						 'mcc': 'MCC', 'mnc': 'MNC'}, inplace=True)
			LTEData = lteData[
				['sitename', 'cellname', 'earfcndl', 'status', 'band', 'eci', 'pci', 'tac', 'longitude', 'latitude', \
				 'azimuth', 'tech', 'Mech. Downtilt', 'Elec. Downtilt', 'Total Tilt', 'beamwidth', '', 'MCC', 'MNC',
				 'operator']]
			# print('ltedata',LTEData)
			# elif request.form['action'] == 'Import_NR':
			nrcsv = request.files.get('nrData')
			nrData = pd.read_csv(nrcsv)
			nrData['operator'] = 'T-Mobile'
			nrData["Total Tilt"] = nrData[['m_dtilts', 'e_dtilts']].sum(axis=1)
			nrData[''] = ''
			nrData['band'] = ''
			nrData.rename(columns={'siteid': 'sitename', 'cell': 'cellname', 'nrarfcndl': 'earfcndl', 'nrcellid': 'eci', \
								   'physicalcellid': 'pci', 'orientation': 'azimuth', 'm_dtilts': 'Mech. Downtilt',
								   'e_dtilts': 'Elec. Downtilt', \
								   'beam_width': 'beamwidth', 'mcc': 'MCC', 'mnc': 'MNC'}, inplace=True)
			NRData = nrData[
				['sitename', 'cellname', 'earfcndl', 'status', 'band', 'eci', 'pci', 'tac', 'longitude', 'latitude', \
				 'azimuth', 'tech', 'Mech. Downtilt', 'Elec. Downtilt', 'Total Tilt', 'beamwidth', '', 'MCC', 'MNC',
				 'operator']]
			# print('nrdata',NRData)

			output_path = os.path.join(tempfile._get_default_tempdir(), next(tempfile._get_candidate_names()))
			os.mkdir(output_path)

			export_name = 'Site configuration for BIGOS_' + '_' + time.strftime("%Y%m%d-%H%M%S") + '.xlsx'

			path = os.path.join(output_path, 'Export_Test.xlsx')
			result_export = pd.ExcelWriter(path)

			GSMdata.to_excel(result_export, startrow=0, index=False, merge_cells=False, sheet_name="2G")
			UMTSData.to_excel(result_export, startrow=0, index=False, merge_cells=False, sheet_name="3G")
			LTEData.to_excel(result_export, startrow=0, index=False, merge_cells=False, sheet_name="4G")
			NRData.to_excel(result_export, startrow=0, index=False, merge_cells=False, sheet_name="5G")

			result_export.save()
			return send_file(result_export, attachment_filename=export_name, as_attachment=True)

	return render_template('Dashboard/BIGOS_formatExport.html', title='BIGOS Data Format', form=form)