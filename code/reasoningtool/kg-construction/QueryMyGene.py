''' This module defines the class QueryProteinEntity. QueryProteinEntity class is designed
to query protein entity from mygene library. The
available methods include:

    get_protein_entity : query protein properties by ID
    get_microRNA_entity : query micro properties by ID

'''

__author__ = 'Deqing Qu'
__copyright__ = 'Oregon State University'
__credits__ = ['Deqing Qu', 'Stephen Ramsey']
__license__ = 'MIT'
__version__ = '0.1.0'
__maintainer__ = ''
__email__ = ''
__status__ = 'Prototype'

import mygene
import requests_cache
import json

# configure requests package to use the "orangeboard.sqlite" cache
requests_cache.install_cache('orangeboard')

class QueryMyGene:

    @staticmethod
    def get_protein_entity(protein_id):
        mg = mygene.MyGeneInfo()
        results = str(mg.query(protein_id, fields='all', return_raw='True'))
        result_str = 'UNKNOWN'
        if len(results) > 100:
            json_dict = json.loads(results)
            result_str = json.dumps(json_dict)
        return result_str

    @staticmethod
    def get_microRNA_entity(microrna_id):
        mg = mygene.MyGeneInfo()
        results = str(mg.query(microrna_id.replace('NCBIGene', 'entrezgene'), fields='all', return_raw='True'))
        result_str = 'UNKNOWN'
        if len(results) > 100:
            json_dict = json.loads(results)
            result_str = json.dumps(json_dict)
        return result_str

if __name__ == '__main__':

    def save_to_test_file(key, value):
        f = open('test_data.json', 'r+')
        try:
            json_data = json.load(f)
        except ValueError:
            json_data = {}
        f.seek(0)
        f.truncate()
        json_data[key] = value
        json.dump(json_data, f)
        f.close()

    save_to_test_file('UniProt:O60884', QueryMyGene.get_protein_entity("UniProt:O60884"))
    save_to_test_file('NCBIGene: 100847086', QueryMyGene.get_microRNA_entity("NCBIGene: 100847086"))